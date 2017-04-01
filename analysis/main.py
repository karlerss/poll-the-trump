from twarc import Twarc
from textblob import TextBlob
import pickle
from models import *
import json

init_db()

t = Twarc('BAVSuRNiZ0IGb5CzIlyHzT1Fd',
          'XVDj8C2SMLzMNaUTrJP3a8UqhHDvYQKZIRIJ9awHDVRBuqxtGD',
          '2433228254-RX73xhPl1dQCEBe7zxhz4cgIJQiL5rUKMofBnz5',
          '33Ju7kmGFPKUXT7AbZ5Nj2ADzaMSL832eur2qwnbFqomt')

pos_sum = 0
count = 0

tweets = list()

for tweet in t.search("to:realdonaldtrump"):
    print tweet['id']
    print tweet['in_reply_to_status_id']
    print tweet['created_at']
    print tweet['text'].encode('utf-8')
    blob = TextBlob(tweet['text'])
    print(blob.sentiment.polarity)
    print pos_sum
    tweet['sentiment'] = blob.sentiment.polarity
    tweets.append(tweet)
    if '#yayfortrump' in tweet['text'] and '#nayfortrump' not in tweet['text']:
        vote = 1
    elif '#yayfortrump' not in tweet['text'] and '#nayfortrump' in tweet['text']:
        vote = -1
    elif blob.sentiment.polarity > 0:
        vote = 1
    elif blob.sentiment.polarity < 0:
        vote = -1
    else:
        vote = 0

    t = Tweet(id=tweet['id'], sentiment=tweet['sentiment'], reply_id=tweet['in_reply_to_status_id'],
              user_id=tweet['user']['id'], vote=vote, json=tweet)

    try:
        db_session().begin(subtransactions=True)
        db_session().add(t)
        db_session().commit()
    except Exception, e:
        db_session().rollback()
        print str(e)

    print "========================"
    count += 1
