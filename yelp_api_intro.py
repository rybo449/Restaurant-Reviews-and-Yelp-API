import rauth
import time
import csv
import re

f = open('names.csv','r')
reader = csv.reader(f, delimiter = ',')
names = []
for i in reader:
	names.append(i)
f.close()


def main():
	api_calls = []
	for name, zipcode, cuisine, phone in names:
		params = get_search_parameters(name, zipcode, cuisine, phone)
		api_calls.append(get_results(params))
		#Be a good internet citizen and rate-limit yourself
		#print api_calls
		for i in api_calls:
			#print i.keys()
			for j in i['businesses']:
				categories = {}
				for k in j.keys():
					if k == "rating" or k == "review_count" or k == "name" or k == "categories":
						try:
							temp = str(j[k])
							if k == 'categories':

								type_cuisine = str()
								for list1 in j[k]:
									for list2 in list1:
										type_cuisine = type_cuisine + ";" + list2

										
								print type_cuisine[1:],
							else:
								
								print temp,",", 
						except:
							continue
				print
		
	##Do other processing	

def get_results(params):

	#Obtain these from Yelp's manage access page
	consumer_key = 'PnHvincoddn76xfpm3LhLg'
	consumer_secret = 'PGmBEyjY0dKu1jzYkJr2Mxe2SCs'
	token = 'Xo8UWIL1CdyTxn-cX-XYbxsAXQOpgfYz'
	token_secret = '1J60nMB-wGTsLyNOyGkY9EZfMFM'

  	#consumer_key = "YOUR_KEY"
	#consumer_secret = "YOUR_SECRET"
	#token = "YOUR_TOKEN"
	#token_secret = "YOUR_TOKEN_SECRET"
	
	session = rauth.OAuth1Session(
		consumer_key = consumer_key
		,consumer_secret = consumer_secret
		,access_token = token
		,access_token_secret = token_secret)
		
	request = session.get("http://api.yelp.com/v2/search",params=params)
	
	#Transforms the JSON API response into a Python dictionary
	data = request.json()
	session.close()
	
	return data
		
def get_search_parameters(name, zipcode, cuisine, phone):
	#See the Yelp API for more details
	params = {}
	params["term"] = name
	#params["postal_code"] = zipcode
	#params["ll"] = "{},{}".format(str(lat),str(long))
	#params["radius_filter"] = "2000"
	params["location"] = zipcode

	return params

if __name__=="__main__":
	main()