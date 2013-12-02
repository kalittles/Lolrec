# Kalil Armstrong
# Lol Recommender
import json
from bs4 import BeautifulSoup
import requests
import collections
from pprint import pprint

#class topRanked:

#Retrieves recent champions
def retrieveRecent(summoner):
	recentChampions = []
	snip1 = 'https://teemojson.p.mashape.com/player/na/'
	snip2 = '/recent_games'
	url = snip1+summoner+snip2
	print "Retrieving results from " + url + " for summoner " + summoner
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
			print "Appended: " + str(x['championId'])
	print '\n'
	print "Champions retrieved."
	print recentChampions
	print "Filtering duplicates." + '\n'
	
	#Filters duplicate names
	filteredChampions = list(collections.Counter(recentChampions))
	print "Filter Complete. New list: "
	print filteredChampions
	print '\n'
	return filteredChampions
	
	#create mapping between champ id and champ internal name
def generateMapping():
	champions = {"aatrox":{"name":"Aatrox","file":"aatrox","champion_id":"266","internal_name":"aatrox"},"ahri":{"name":"Ahri","file":"ahri","champion_id":"103","internal_name":"ahri"},"akali":{"name":"Akali","file":"akali","champion_id":"84","internal_name":"akali"},"alistar":{"name":"Alistar","file":"alistar","champion_id":"12","internal_name":"alistar"},"amumu":{"name":"Amumu","file":"amumu","champion_id":"32","internal_name":"amumu"},"anivia":{"name":"Anivia","file":"anivia","champion_id":"34","internal_name":"anivia"},"annie":{"name":"Annie","file":"annie","champion_id":"1","internal_name":"annie"},"ashe":{"name":"Ashe","file":"ashe","champion_id":"22","internal_name":"ashe"},"blitzcrank":{"name":"Blitzcrank","file":"blitzcrank","champion_id":"53","internal_name":"blitzcrank"},"brand":{"name":"Brand","file":"brand","champion_id":"63","internal_name":"brand"},"caitlyn":{"name":"Caitlyn","file":"caitlyn","champion_id":"51","internal_name":"caitlyn"},"cassiopeia":{"name":"Cassiopeia","file":"cassiopeia","champion_id":"69","internal_name":"cassiopeia"},"cho'gath":{"name":"Cho'Gath","file":"chogath","champion_id":"31","internal_name":"chogath"},"corki":{"name":"Corki","file":"corki","champion_id":"42","internal_name":"corki"},"darius":{"name":"Darius","file":"darius","champion_id":"122","internal_name":"darius"},"diana":{"name":"Diana","file":"diana","champion_id":"131","internal_name":"diana"},"dr. mundo":{"name":"Dr. Mundo","file":"drmundo","champion_id":"36","internal_name":"dr. mundo"},"draven":{"name":"Draven","file":"draven","champion_id":"119","internal_name":"draven"},"elise":{"name":"Elise","file":"elise","champion_id":"60","internal_name":"elise"},"evelynn":{"name":"Evelynn","file":"evelynn","champion_id":"28","internal_name":"evelynn"},"ezreal":{"name":"Ezreal","file":"ezreal","champion_id":"81","internal_name":"ezreal"},"fiddlesticks":{"name":"Fiddlesticks","file":"fiddlesticks","champion_id":"9","internal_name":"fiddlesticks"},"fiora":{"name":"Fiora","file":"fiora","champion_id":"114","internal_name":"fiora"},"fizz":{"name":"Fizz","file":"fizz","champion_id":"105","internal_name":"fizz"},"galio":{"name":"Galio","file":"galio","champion_id":"3","internal_name":"galio"},"gangplank":{"name":"Gangplank","file":"gangplank","champion_id":"41","internal_name":"gangplank"},"garen":{"name":"Garen","file":"garen","champion_id":"86","internal_name":"garen"},"gragas":{"name":"Gragas","file":"gragas","champion_id":"79","internal_name":"gragas"},"graves":{"name":"Graves","file":"graves","champion_id":"104","internal_name":"graves"},"hecarim":{"name":"Hecarim","file":"hecarim","champion_id":"120","internal_name":"hecarim"},"heimerdinger":{"name":"Heimerdinger","file":"heimerdinger","champion_id":"74","internal_name":"heimerdinger"},"irelia":{"name":"Irelia","file":"irelia","champion_id":"39","internal_name":"irelia"},"janna":{"name":"Janna","file":"janna","champion_id":"40","internal_name":"janna"},"jarvan iv":{"name":"Jarvan IV","file":"jarvaniv","champion_id":"59","internal_name":"jarvan iv"},"jax":{"name":"Jax","file":"jax","champion_id":"24","internal_name":"jax"},"jayce":{"name":"Jayce","file":"jayce","champion_id":"126","internal_name":"jayce"},"jinx":{"name":"Jinx","file":"jinx","champion_id":"222","internal_name":"jinx"},"karma":{"name":"Karma","file":"karma","champion_id":"43","internal_name":"karma"},"karthus":{"name":"Karthus","file":"karthus","champion_id":"30","internal_name":"karthus"},"kassadin":{"name":"Kassadin","file":"kassadin","champion_id":"38","internal_name":"kassadin"},"katarina":{"name":"Katarina","file":"katarina","champion_id":"55","internal_name":"katarina"},"kayle":{"name":"Kayle","file":"kayle","champion_id":"10","internal_name":"kayle"},"kennen":{"name":"Kennen","file":"kennen","champion_id":"85","internal_name":"kennen"},"kha'zix":{"name":"Kha'Zix","file":"khazix","champion_id":"121","internal_name":"khazix"},"kog'maw":{"name":"Kog'Maw","file":"kogmaw","champion_id":"96","internal_name":"kog'maw"},"leblanc":{"name":"LeBlanc","file":"leblanc","champion_id":"7","internal_name":"leblanc"},"lee sin":{"name":"Lee Sin","file":"leesin","champion_id":"64","internal_name":"LeeSin"},"leona":{"name":"Leona","file":"leona","champion_id":"89","internal_name":"leona"},"lissandra":{"name":"Lissandra","file":"lissandra","champion_id":"127","internal_name":"lissandra"},"lucian":{"name":"Lucian","file":"lucian","champion_id":"236","internal_name":"lucian"},"lulu":{"name":"Lulu","file":"lulu","champion_id":"117","internal_name":"lulu"},"lux":{"name":"Lux","file":"lux","champion_id":"99","internal_name":"lux"},"malphite":{"name":"Malphite","file":"malphite","champion_id":"54","internal_name":"malphite"},"malzahar":{"name":"Malzahar","file":"malzahar","champion_id":"90","internal_name":"malzahar"},"maokai":{"name":"Maokai","file":"maokai","champion_id":"57","internal_name":"maokai"},"master yi":{"name":"Master Yi","file":"masteryi","champion_id":"11","internal_name":"master yi"},"miss fortune":{"name":"Miss Fortune","file":"missfortune","champion_id":"21","internal_name":"miss fortune"},"mordekaiser":{"name":"Mordekaiser","file":"mordekaiser","champion_id":"82","internal_name":"mordekaiser"},"morgana":{"name":"Morgana","file":"morgana","champion_id":"25","internal_name":"morgana"},"nami":{"name":"Nami","file":"nami","champion_id":"267","internal_name":"nami"},"nasus":{"name":"Nasus","file":"nasus","champion_id":"75","internal_name":"nasus"},"nautilus":{"name":"Nautilus","file":"nautilus","champion_id":"111","internal_name":"nautilus"},"nidalee":{"name":"Nidalee","file":"nidalee","champion_id":"76","internal_name":"nidalee"},"nocturne":{"name":"Nocturne","file":"nocturne","champion_id":"56","internal_name":"nocturne"},"nunu":{"name":"Nunu","file":"nunu","champion_id":"20","internal_name":"nunu"},"olaf":{"name":"Olaf","file":"olaf","champion_id":"2","internal_name":"olaf"},"orianna":{"name":"Orianna","file":"orianna","champion_id":"61","internal_name":"orianna"},"pantheon":{"name":"Pantheon","file":"pantheon","champion_id":"80","internal_name":"pantheon"},"poppy":{"name":"Poppy","file":"poppy","champion_id":"78","internal_name":"poppy"},"quinn":{"name":"Quinn","file":"quinn","champion_id":"133","internal_name":"quinn"},"rammus":{"name":"Rammus","file":"rammus","champion_id":"33","internal_name":"rammus"},"renekton":{"name":"Renekton","file":"renekton","champion_id":"58","internal_name":"renekton"},"rengar":{"name":"Rengar","file":"rengar","champion_id":"107","internal_name":"rengar"},"riven":{"name":"Riven","file":"riven","champion_id":"92","internal_name":"riven"},"rumble":{"name":"Rumble","file":"rumble","champion_id":"68","internal_name":"rumble"},"ryze":{"name":"Ryze","file":"ryze","champion_id":"13","internal_name":"ryze"},"sejuani":{"name":"Sejuani","file":"sejuani","champion_id":"113","internal_name":"sejuani"},"shaco":{"name":"Shaco","file":"shaco","champion_id":"35","internal_name":"shaco"},"shen":{"name":"Shen","file":"shen","champion_id":"98","internal_name":"shen"},"shyvana":{"name":"Shyvana","file":"shyvana","champion_id":"102","internal_name":"shyvana"},"singed":{"name":"Singed","file":"singed","champion_id":"27","internal_name":"singed"},"sion":{"name":"Sion","file":"sion","champion_id":"14","internal_name":"sion"},"sivir":{"name":"Sivir","file":"sivir","champion_id":"15","internal_name":"sivir"},"skarner":{"name":"Skarner","file":"skarner","champion_id":"72","internal_name":"skarner"},"sona":{"name":"Sona","file":"sona","champion_id":"37","internal_name":"sona"},"soraka":{"name":"Soraka","file":"soraka","champion_id":"16","internal_name":"soraka"},"swain":{"name":"Swain","file":"swain","champion_id":"50","internal_name":"swain"},"syndra":{"name":"Syndra","file":"syndra","champion_id":"134","internal_name":"syndra"},"talon":{"name":"Talon","file":"talon","champion_id":"91","internal_name":"talon"},"taric":{"name":"Taric","file":"taric","champion_id":"44","internal_name":"taric"},"teemo":{"name":"Teemo","file":"teemo","champion_id":"17","internal_name":"teemo"},"thresh":{"name":"Thresh","file":"thresh","champion_id":"412","internal_name":"thresh"},"tristana":{"name":"Tristana","file":"tristana","champion_id":"18","internal_name":"tristana"},"trundle":{"name":"Trundle","file":"trundle","champion_id":"48","internal_name":"trundle"},"tryndamere":{"name":"Tryndamere","file":"tryndamere","champion_id":"23","internal_name":"tryndamere"},"twisted fate":{"name":"Twisted Fate","file":"twistedfate","champion_id":"4","internal_name":"twisted fate"},"twitch":{"name":"Twitch","file":"twitch","champion_id":"29","internal_name":"twitch"},"udyr":{"name":"Udyr","file":"udyr","champion_id":"77","internal_name":"udyr"},"urgot":{"name":"Urgot","file":"urgot","champion_id":"6","internal_name":"urgot"},"varus":{"name":"Varus","file":"varus","champion_id":"110","internal_name":"varus"},"vayne":{"name":"Vayne","file":"vayne","champion_id":"67","internal_name":"vayne"},"veigar":{"name":"Veigar","file":"veigar","champion_id":"45","internal_name":"veigar"},"vi":{"name":"Vi","file":"vi","champion_id":"254","internal_name":"vi"},"viktor":{"name":"Viktor","file":"viktor","champion_id":"112","internal_name":"viktor"},"vladimir":{"name":"Vladimir","file":"vladimir","champion_id":"8","internal_name":"vladimir"},"volibear":{"name":"Volibear","file":"volibear","champion_id":"106","internal_name":"volibear"},"warwick":{"name":"Warwick","file":"warwick","champion_id":"19","internal_name":"warwick"},"wukong":{"name":"Wukong","file":"monkeyking","champion_id":"62","internal_name":"wukong"},"xerath":{"name":"Xerath","file":"xerath","champion_id":"101","internal_name":"xerath"},"xin zhao":{"name":"Xin Zhao","file":"xinzhao","champion_id":"5","internal_name":"xin zhao"},"yorick":{"name":"Yorick","file":"yorick","champion_id":"83","internal_name":"yorick"},"zac":{"name":"Zac","file":"zac","champion_id":"154","internal_name":"zac"},"zed":{"name":"Zed","file":"zed","champion_id":"238","internal_name":"zed"},"ziggs":{"name":"Ziggs","file":"ziggs","champion_id":"115","internal_name":"ziggs"},"zilean":{"name":"Zilean","file":"zilean","champion_id":"26","internal_name":"zilean"},"zyra":{"name":"Zyra","file":"zyra","champion_id":"143","internal_name":"zyra"}}
	newdict = {}
	subdict = {} #will have internal and normal name
	for x in champions:
		a = str(champions[x]["champion_id"])
		b = champions[x]["name"]
		c = champions[x]["internal_name"]
		newdict[a] = {}
		newdict[a]['name'] = b
		newdict[a]['internal_name'] = c
	
	print "Generating Mapping Champion Names and Champion Identification Numbers"
	print newdict
	print "Complete" + '\n'
	return newdict
	
#Pulls list of champions. 
#Receives a map that is of the form ID:(name/internalname)
#are a list of dictionaries of champions in the same role
def retrieveChampions(champs, map):

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
	print "Internal names:"
	print internalnames
	print '\n'
	
	for x in internalnames:
		a = internalnames[x]['internal_name'].title()
		if a == "Leesin":
			a = "LeeSin"
		if a == "Fiddlesticks":
			a = "FiddleSticks"
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
	print "Printing core champions."
	print coreChamps
	print "Done."
	print '\n'
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
def StatScrape(champs, map): #Champs is core champs
	#supposed to use champs
	r = requests.get('http://www.lolking.net/champions/')
	soup = BeautifulSoup(r.content) #of type response
	
	final = []
	table = {}

	for x in champs:
		print "x" + str(x)
		for y in champs[x]: # y is the entire dictionary
			for key in y.keys():
				var = y[key]['name']
				print "Champ ID: " + str(var)
				td_name = soup.find('td',{"data-sortval":var})
				tr = td_name.parent
				pr = (tr.find_all('td',recursive=False)[3].text).strip('%')
				wr = (tr.find_all('td',recursive=False)[4].text).strip('%')
				br = (tr.find_all('td',recursive=False)[5].text).strip('%')
		
		
				print "Pickrate: " + pr
				print "Winrate: " + wr
				print "Banrate: " + br
		
				table[key] = {}
				table[key]['pr'] = pr
				table[key]['wr'] = wr
				table[key]['br'] = br
				table[key]['ori'] = x #Original champion it was recommended by
	return table
				
	# for x in champions:
		# var = champions[x]["name"]
		# #Map back 
		# #Actual search
		# td_name = soup.find('td',{"data-sortval":var})
		# tr = td_name.parent
		# print x
		# pr = (tr.find_all('td',recursive=False)[3].text).strip('%')
		# wr = (tr.find_all('td',recursive=False)[4].text).strip('%')
		# br = (tr.find_all('td',recursive=False)[5].text).strip('%')
		
		
		# print "Pickrate: " + pr
		# print "Winrate: " + wr
		# print "Banrate: " + br
		
		# table[x] = {}
		# table[x]['pr'] = pr
		# table[x]['wr'] = wr
		# table[x]['br'] = br
	# return table

def tempRank(table):
	ranked = {}
	for x in table:
		print table[x]['wr']
		rank = (float(table[x]['wr']) - float(table[x]['br'])) * (2*float(table[x]['pr']))
		ranked[x] = {}
		ranked[x]['rank'] = rank
		ranked[x]['original_champion_id'] = table[x]['ori']
		ranked[x]['champion_name'] = ""
		ranked[x]['original_champion_name'] = ""
	return ranked

def idToName(ranked):
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
	pprint(ranked)
class Ranker:
	def __init__(self, champions):
		print "hi"
		#thinking winrate - banrate + popularity



if __name__=="__main__":
	champs = retrieveRecent("sarahfan03")
	corechamps = retrieveChampions(champs, generateMapping() )
	table = StatScrape(corechamps, generateMapping)
	tempR = tempRank(table)
	idToName(tempR)
