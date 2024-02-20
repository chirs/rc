
import json
import pymongo
import tweepy
import urllib2



# These really shouldn't be here. (especially the ones marked secret)
consumer_key = 'MNeiEaTLAWKwK1j9sVEVZQ'
consumer_secret = 'db5qZKh4uPO2H1SQnp58tNAe8SbxlkUkKTnBPV1WUc'

access_token = '14590503-d5UejzdiOXuX9HrhncmfFGCVtdzuIkQXJz1TZ1lfI'
access_token_secret = 'JORxsGkYU9kOp8bc26CueUOFx9v4iGmEJJII0xg8tQ'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


connection = pymongo.Connection()

db = connection.twitpope
unfiltered_tweets = db.unfiltered
processed_tweets = db.processed


def write_since(sid):
    f = open('since', 'w')
    f.write(str(sid))
    f.close()

def get_since():
    try:
        return open('since').read()
    except:
        return 0


def search_twitter(keyword):
    sid = get_since()

    # Am using old search api. 
    # Don't want to get back wrapped objects from an api call - just json / dicts.
    #url = 'https://api.twitter.com/1.1/search/tweets.json?q=%s&count=80&since_id=%s' % (keyword, sid)
    url = 'http://search.twitter.com/search.json?q=%s&rpp=100&since_id=%s' % (keyword, sid)
    s = urllib2.urlopen(url).read()
    tjson = json.loads(s)
    write_since(tjson['max_id'])
    return tjson['results']


def insert_rows(collection, rows):
    for row in rows:
        collection.insert(row)

    
def scrape():
    # Do a round of scraping.
    rows = search_twitter('pope')
    insert_rows(unfiltered_tweets, rows)
    

if __name__ == "__main__":
    scrape()
