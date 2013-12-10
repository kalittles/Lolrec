# Kalil Armstrong
# Lol Recommender
import time
import fileinput
import json
from bs4 import BeautifulSoup
import requests
import collections
import bottle
from pprint import pprint
from bottle import route, run, template

class Ranker:
	def __init__(self):
		print None
		#thinking winrate - banrate + popularity
	#Retrieves recent champions
	def retrieveRecent(self, summoner):
		recentChampions = []
		snip1 = 'https://teemojson.p.mashape.com/player/na/'
		snip2 = '/recent_games'
		url = snip1+summoner+snip2
		#print "Retrieving results from " + url + " for summoner " + summoner
		payload = {'games':'data'}
		headers = {"X-Mashape-Authorization": "qJAbF1ZlgsHWLb1wwIcMcwOVOlSCZ6EL"}
		r = requests.post(url, data = json.dumps(payload), headers = headers)
	
	#Pulls champion names, removes null values
		recentMatches = r.json()
		recentArray = recentMatches['data']['gameStatistics']['array']
		for x in recentArray:
			if x['championId'] == None:
				print "Null detected."
			else:
				recentChampions.append(x['championId'])
				#print "Appended: " + str(x['championId'])
		#print '\n'
	#	print "Champions retrieved."
		#print recentChampions
		#print "Filtering duplicates." + '\n'
	
	#Filters duplicate names
		filteredChampions = list(collections.Counter(recentChampions))
		#print "Filter Complete. New list: "
		#print filteredChampions
		#print '\n'
		return filteredChampions
	
	#create mapping between champ id and champ internal name
	def generateMapping(self):
		json_data = open('champions.json')
		champions = json.load(json_data)
		#pprint(data)
		json_data.close()
		newdict = {}
		subdict = {} #will have internal and normal name
		for x in champions:
			a = str(champions[x]["champion_id"])
			b = champions[x]["name"]
			c = champions[x]["internal_name"]
			newdict[a] = {}
			newdict[a]['name'] = b
			newdict[a]['internal_name'] = c
		
		#print "Generating Mapping Champion Names and Champion Identification Numbers"
		#print newdict
		#print "Complete" + '\n'
		return newdict
	
#Pulls list of champions. 
#Receives a map that is of the form ID:(name/internalname)
#are a list of dictionaries of champions in the same role
	def retrieveChampions(self, champs, map):

		coreChamps = {}
		internalnames = {} #from ids to names
		payload = {'games':'data'}
		headers = {"X-Mashape-Authorization": "qJAbF1ZlgsHWLb1wwIcMcwOVOlSCZ6EL"}
		url = 'https://teemojson.p.mashape.com/datadragon/champion'
		r = requests.post(url, data = json.dumps(payload), headers = headers)
		#Filter champions based on role
		championList = r.json()
		#Gives you internal names to ids.
		for x in champs:
			for y in map:
				if int(x) == int(y):
					dict = {}
					internalnames[x] = {}
					internalnames[x]['internal_name'] = map[y]['internal_name']
					internalnames[x]['name'] = map[y]['name']
					internalnames[x]['id'] = map[y]
		#print "Internal names:"
		#print internalnames
		#print '\n'
	
		for x in internalnames:
			a = internalnames[x]['internal_name'].title()
			if a == "Leesin":
				a = "LeeSin"
			if a == "Fiddlesticks":
				a = "FiddleSticks"
			if a == "Miss Fortune":
				a = "MissFortune"
			if a == "JarvanIv":
				a = "JarvanIV"
			role = championList['data'][a]['tags']
			for y in championList['data']:
				tempdict = {}
				innerdict = {}
				if role == championList['data'][y]['tags']:
					innerdict['title'] = championList['data'][y]['title']
					#innerdict['blurb'] = championList['data'][y]['blurb']
					innerdict['internal_name'] = championList['data'][y]['name']
					innerdict['name'] = ""
					innerdict ['tfidf'] = ""
					innerdict['key'] = championList['data'][y]['key']
					for j in map:
						if str(j) == innerdict['key']:
							innerdict['name'] = map[str(j)]['name']
					tempdict[championList['data'][y]['key']] = innerdict		#Sets ID equal to all that other crap
					coreChamps.setdefault(championList['data'][a]['key'],[]).append(tempdict) 
	#Fill out name field.
		#print "Printing core champions."
		#print coreChamps
		#print "Done."
		#print '\n'
	#CoreChamps is a dictionary that containst he keys of the target champions. Their values are lists. Within those lists are dictionaries whose keys are that of a similar champion

	#utility
		print "Similarity Array Generated:"
		print coreChamps.keys()
		test = ""
		for x in coreChamps:
			number = str(len(coreChamps[x]))
			print "Similarities for " + x + ": " + number
		print '\n'
		return coreChamps

#Retrieves win rates / ban / popularity for each ranked champion
	def StatScrape(self, champs, map): #Champs is core champs
		#supposed to use champs
		r = requests.get('http://www.lolking.net/champions/')
		soup = BeautifulSoup(r.content) #of type response
	
		final = []
		table = {}

		for x in champs:
			#print "x" + str(x)
			for y in champs[x]: # y is the entire dictionary
				for key in y.keys():
					var = y[key]['name']
					#print "Champ ID: " + str(var)
					td_name = soup.find('td',{"data-sortval":var})
					tr = td_name.parent
					pr = (tr.find_all('td',recursive=False)[3].text).strip('%')
					wr = (tr.find_all('td',recursive=False)[4].text).strip('%')
					br = (tr.find_all('td',recursive=False)[5].text).strip('%')
			
		
					#print "Pickrate: " + pr
					#print "Winrate: " + wr
					#print "Banrate: " + br
		
					table[key] = {}
					table[key]['pr'] = pr
					table[key]['wr'] = wr
					table[key]['br'] = br
					table[key]['ori'] = x #Original champion it was recommended by
		return table
				

	def tempRank(self, table):
		ranked = {}
		for x in table:
			#print table[x]['wr']
			rank = (float(table[x]['wr']) - float(table[x]['br'])) * (2*float(table[x]['pr']))
			ranked[x] = {}
			ranked[x]['rank'] = rank
			ranked[x]['original_champion_id'] = table[x]['ori']
			ranked[x]['champion_name'] = ""
			ranked[x]['original_champion_name'] = ""
		return ranked

	def idToName(self, ranked):
		json_data = open('champions.json')
		data = json.load(json_data)
		#pprint(data)
		json_data.close()
		for x in data:
			for y in ranked:
				if data[x]['champion_id'] == y:
					ranked[y]['champion_name'] = data[x]['name']
				if data[x]['champion_id'] == ranked[y]['original_champion_id']:
					ranked[y]['original_champion_name'] = data[x]['name']
		
		#organizer = []
		#organized = {}
		#for x in ranked:
			#print x
			#organized[ranked[x]['original_champion_name']] = {}
			#champs = []
			#organized[ranked[x]['original_champion_name']]['champion'] = ranked[x]['champion_name']
			#organized[ranked[x]['original_champion_name']]['score'] = ranked[x]['rank']
			#print ranked[x]['champion_name']
			#print ranked[x]['rank']
			#organizer.append(organized)
		#pprint(ranked)
		for x in ranked:
			print "Champion Recommended:"
			print ranked[x]['champion_name']
			print "Original Champion: "
			print ranked[x]['original_champion_name']
			print "Score: "
			print ranked[x]['rank']
			print "\n"
			
		return ranked
		
	final = {}

_searcher = None

@bottle.route('/search')
def search(name='World'):
    global _searcher
    query = bottle.request.query.q
    start_time = time.time()
    tweets = _searcher.retrieveRecent(query)
    coreChamps = _searcher.retrieveChampions(tweets, _searcher.generateMapping() )
    table = _searcher.StatScrape(coreChamps, _searcher.generateMapping)
    tempR = _searcher.tempRank(table)
    _searcher.final = _searcher.idToName(tempR)
    end_time = time.time()
    print end_time
    pprint(_searcher.final)
    return dict(
		tweets = _searcher.final,
		count = len(tweets),
		time = end_time - start_time,
	)
	
def magic():
	ranker = Ranker()
	champs = ranker.retrieveRecent("sarahfan03")
	corechamps = ranker.retrieveChampions(champs, ranker.generateMapping() )
	table = ranker.StatScrape(corechamps, ranker.generateMapping)
	tempR = ranker.tempRank(table)
	ranker.final = ranker.idToName(tempR)
@bottle.route('/')
def index():
    return bottle.static_file('index.html', root='static')
	
@bottle.route('/static/<filename:path>')
def server_static(filename):
    return bottle.static_file(filename, root='static')


if __name__=="__main__":
	_searcher = Ranker()
	#magic()
	bottle.run(host='localhost',
               port=8080,
               reloader=True)
	#pprint("TEST TEST TEST")
	#pprint(ranker.final)
	#app.run()
