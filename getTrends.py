import requests
import json
import time
import sys
import re
import os
import pprint

pp=pprint.PrettyPrinter(indent=2)



if len(sys.argv)<2:
	print ("Error, you need to specify your query: python {} <QUERY> [<FILE>] [<LOCALE>]".format(sys.argv[0]))
	exit()

QUERY=sys.argv[1]



if len(sys.argv)>=3:
	OUTPUT_FILE=re.sub(".csv|.json", "", sys.argv[2])
	PRETTY=0
else:
	PRETTY=1

if(len(sys.argv)==4):
	LOCALE=sys.argv[3]
else:
	LOCALE="en-US"




TOKEN=None

BASE_URL="https://trends.google.com/trends/api/widgetdata/multiline?hl="+LOCALE+"&tz=240"



def getToken(query):
	global TOKEN
	print("Aquiring Token")
	query_token={"comparisonItem":[{"keyword":query,"geo":"","time":"today 5-y"}],"category":"0" , "property":""}
	url="https://trends.google.com/trends/api/explore?hl="+LOCALE+"&tz=240&req="+json.dumps(query_token)+"&tz=300"
	req=requests.get(url)
	if(req.ok):
		TOKEN=json.loads(req.text.split("\n")[1]).get("widgets", "empty")[0].get("token")
	else:
		print ("There is some kind of error with the request: Code-> {}".format(res.status_code))



def applySomeLogic(text):
	if(PRETTY==1):
		print ("Resulting Output")
		pp.pprint(json.loads(text))
	else:
		JSON=json.loads(text)
		elems=JSON.get("default", {}).get("timelineData")
		if (len(elems)>0):
			with open("./"+OUTPUT_FILE+".json", 'w') as f:
				for elem in elems:
					f.write(json.dumps(elem)+"\n")
		
			print("Successfully writen to: {}.json".format(OUTPUT_FILE))
		else:
			print("ERROR-> The result list is empty: No result")
	




print("********************PROGRAM STARTING********************")

getToken(QUERY)
previous=time.gmtime(time.time()- 31557600*5)
request={"time":"{} {}".format(time.strftime("%Y-%m-%d", previous), time.strftime("%Y-%m-%d")),"resolution":"WEEK","locale":LOCALE,"comparisonItem":[{"geo":{},"complexKeywordsRestriction":{"keyword":[{"type":"BROAD","value":QUERY}]}}],"requestOptions":{"property":"","backend":"IZG","category":0}}
url=BASE_URL+"&req="+json.dumps(request)+"&token="+TOKEN
res=requests.get(url)
if(res.ok):
	myjson=res.text.split("\n")[1]
	applySomeLogic(myjson)
else:
	print ("There is some kind of error with the request: Code-> {}".format(res.status_code))


print("*****************END PROGRAM****************************")