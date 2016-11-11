import tweepy
# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.
#
# You will demo this live for grading.

print("""No output necessary although you 
	can print out a success/failure message if you want to.""")

import tweepy, time, sys

#argfile = str(sys.argv[1])


CONSUMER_KEY = 'pzsBRxMWGnm5ivFWZ8Dy2IQsa'
CONSUMER_SECRET = 'nJNjFLhiunz2snIIFUgANq63ChDl3TeS7zzOF3AKUH2qQUgf27'
ACCESS_KEY = '796776439685279744-3TlOVpwnjfWhqanChpZu7ibIA4nevWR'
ACCESS_SECRET = 'YNYengDGGpoKfJ3Wr6pfgpCUJj3Ak2YvdVCFrdlc3a5xe'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

picture = '/Users/tommykidd/Desktop/miscellaneous/nightsky.png'
#picture = 'nightsky.png'
message = "#UMSI206 #Proj3"

api.update_with_media(picture, message)




#Posting a picture to twitter using tweepy
# import sys
# import tweepy
# import os

# auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
# auth.secure = True
# auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
# # access the Twitter API using tweepy with OAuth
# api = tweepy.API(auth) 
# #getting the parameter passed via the shell command from the Arduino Sketch
# status = status = sys.argv[1] 
# fn = os.path.abspath('/mnt/sda1/moneyplant.png')
# #UpdateStatus of twitter called with the image file
# api.update_with_media(fn, status=status)








































# # Unique code from Twitter
# access_token = "369278035-UrnJsXhuc6wJZ0A3W7HFs3EWtJ1MkDpbGUVCo1uF"
# access_token_secret = "elWZhMQpBxXNVhXbPoPR4KAu3DjERVJJ8GqW5AAW79R9v"
# consumer_key = "T4PhmbsxdwMIml8h1TrUF13BJ"
# consumer_secret = "ZT2Ed83oROantt4jETjjhmaTJH24BxhWYcKk04H1fsTzzsqcNE"

# # Boilerplate code here
# auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
# auth.set_access_token(access_token,access_token_secret)

# theApi = tweepy.API(auth)
############
# import requests
# import os


# def twitter_api():
#     access_token = config.get('twitter_credentials', 'access_token')
#     access_token_secret = config.get('twitter_credentials', 'access_token_secret')
#     consumer_key = config.get('twitter_credentials', 'consumer_key')
#     consumer_secret = config.get('twitter_credentials', 'consumer_secret')

#     auth = OAuthHandler(consumer_key, consumer_secret)
#     auth.set_access_token(access_token, access_token_secret)
#     api = API(auth)
#     return api
# ############


# def tweet_image(url, message):
#     api = twitter_api()
#     filename = 'Screenshot 2016-05-23 18.36.49'
#     request = requests.get(url, stream=True)
#     if request.status_code == 200:
#         with open(filename, 'wb') as image:
#             for chunk in request:
#                 image.write(chunk)

#         api.update_with_media(filename, status=message)
#         os.remove(filename)
#     else:
#         print("Unable to download image")


# url = "http://animalia-life.com/data_images/bird/bird1.jpg"
# message = "#UMSI-206 #Proj3"
# tweet_image(url, message)




