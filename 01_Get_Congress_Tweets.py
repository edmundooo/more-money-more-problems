'''
Subject: Topics of Tweets of Congress through the Lens 
         of Campaign Finance

Date: 09/08/2018

Name: Edmund D. Chitwood

Summary:

The following script uses Jefferson Enrique's got (Get Old 
Tweets) module to get the Tweets of all the current members of
the US Congress, and reads the Tweets and select Tweet
metadata into CSV files.

'''

# got source: https://github.com/edmundooo/GetOldTweets-python
# got is writtn in Python 2
import got
import csv
import shutil

# Access CSV file that contains twitter handles of current 
# Members of the US congressm as of May 23, 2017
# Source for House of Representatives: 
# https://gwu-libraries.github.io/sfm-ui/resources/115th-Congress-House-seeds.csv
# Source for Senate: 
# https://gwu-libraries.github.io/sfm-ui/resources/115th-Congress-Senate-seeds.csv 
with open("115th-Congress-seeds.csv") as f:
        twitter_handles = [row.split(',')[0] for row in f]

# Get Tweets and Tweet metadata for each current member 
# of the US Congress
for handle in twitter_handles:

	tweetCriteria = got.manager.TweetCriteria().setUsername(handle)
	tweet = got.manager.TweetManager.getTweets(tweetCriteria)

    # Create a CSV file to hold the Tweets of each 
    # member and name it based on Twitter handle
	with open(handle+'_tweets.csv', mode='w') as employee_file:
        	employee_writer = csv.writer(employee_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

		for line in tweet:
			encoded_tweet=line.text.encode('utf-8')
			employee_writer.writerow([line.username,line.date,line.retweets,line.favorites,encoded_tweet,line.mentions,line.hashtags,line.id,line.permalink])

    # Move each file into data folder
	shutil.move('/home/ubuntu/data/'+handle+'_tweets.csv', '/home/ubuntu/data/'+handle+'_tweets.csv')
