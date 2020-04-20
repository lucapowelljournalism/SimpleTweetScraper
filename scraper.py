#Type all this. Also, you'll  want to pipenv install tweepy from your command line.
import tweepy
import twitter
import requests
import csv

#Your credentials saved as variables. You get these from twitter. Here is how: https://developer.twitter.com/en/apply-for-access #
consumer_key = 'consumerkeygoeshere'
consumer_secret = 'consumer_secretgoeshere'
access_token = 'accesstokengoeshere'
access_secret = 'accesssecretgoeshere'

#This tells tweepy, the python library we are using, your credentials#
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

#Now you are in Twitter's 'back-end'. You can ask for anything using the 'api' class. For example, to get one tweet you could do this: status = api.get_status(id). You are calling the 'get_status' function on the class 'api' and passing the parameter 'id'. Full documentation is here: https://github.com/tweepy/tweepy
def scrape_tweets(user):
    rows=[]
    public_tweets = api.user_timeline(screen_name=user,tweet_mode='extended',count=120,include_rts=False,exclude_replies=True) #gets the timeline for a variable user
    for tweet in public_tweets:
        singletweet= tweet.full_text #gets the full text of the tweet and storess it in a variable
        date = tweet.created_at #gets the datetime of the tweet and stores it in a variable.
        row = {"tweet":singletweet, "dates": date}
        rows.append(row)
    with open(f'{user}.csv', "w") as csvfile:
        fieldnames = ["tweet","dates"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

                    ##This is where you put your list of usernames##
users=['username1','username2','username3']
for x in users:
    scrape_tweets(x)
