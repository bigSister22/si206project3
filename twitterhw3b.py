# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.

import tweepy
from textblob import TextBlob

# Unique code from Twitter
access_token = "369278035-UrnJsXhuc6wJZ0A3W7HFs3EWtJ1MkDpbGUVCo1uF"
access_token_secret = "elWZhMQpBxXNVhXbPoPR4KAu3DjERVJJ8GqW5AAW79R9v"
consumer_key = "T4PhmbsxdwMIml8h1TrUF13BJ"
consumer_secret = "ZT2Ed83oROantt4jETjjhmaTJH24BxhWYcKk04H1fsTzzsqcNE"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
#Now we can Create Tweets, Delete Tweets, and Find Twitter Users

public_tweets = api.search(input("Enter a search term: "))

sub = 0
subCount = 0
pol = 0
polCount = 0
for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	#analysis.sentiment
	sub+=analysis.sentiment.subjectivity
	if analysis.sentiment.subjectivity != 0:
		subCount+=1
	pol+=analysis.sentiment.polarity
	if analysis.sentiment.polarity !=0:
		polCount+=1

# print (sub)
# print (subCount)
# print (pol)
# print (polCount)


#polarity -- measures how positive or negative
#subjectivity -- measures how factual.

#1 Sentiment Analysis - Understand and Extracting Feelings from Data


print("Average subjectivity is", str(sub/subCount))
print("Average polarity is", str(pol/polCount))
