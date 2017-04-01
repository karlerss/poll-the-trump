from twarc import Twarc
from textblob import TextBlob
import pickle
import models

models.init_db()

t = Twarc('BAVSuRNiZ0IGb5CzIlyHzT1Fd',
          'XVDj8C2SMLzMNaUTrJP3a8UqhHDvYQKZIRIJ9awHDVRBuqxtGD',
          '2433228254-RX73xhPl1dQCEBe7zxhz4cgIJQiL5rUKMofBnz5',
          '33Ju7kmGFPKUXT7AbZ5Nj2ADzaMSL832eur2qwnbFqomt')

pos_sum = 0
count = 0

tweets = list()

for tweet in t.search("impeachtrump"):
    print tweet['in_reply_to_status_id']
    print tweet['created_at']
    print tweet['text'].encode('utf-8')
    blob = TextBlob(tweet['text'])
    print(blob.sentiment.polarity)
    if abs(blob.sentiment.polarity) > 0.5:
        pos_sum += blob.sentiment.polarity
    print pos_sum
    tweet['sentiment'] = blob.sentiment.polarity
    tweets.append(tweet)
    print "========================"
