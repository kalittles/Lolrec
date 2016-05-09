Lolrec
======

LolRec

Simply run python lolrec.py
You can change what summoner it looks up in the main function (it will look up other summoners).

It contacts RIOT's server, pulls champion data, and then pulls the information from the summoner as well.
It then connects to LolKing, scrapes statistics, and then gives an intermediate ranking.

*** NOTICE ***
Note that the k-means clustering algorithm is not implemented in this version - I've moved that to a private repository. Riot now has an official API, so this API being used is now deprecated. This remains posted solely for educational reasons.
