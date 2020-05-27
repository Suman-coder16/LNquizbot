import tweepy 
import time
import sys
import csv
import re
import mechanize
import urllib.request
import random
import time
import datetime
from random import seed, randint

def LNquiz():
    with open ("lnquiz_questions") as f:
     Question = f.readlines()
    post = (list.choice(Question).strip())
    return (post)
     
    #posting question on twitter
    auth = tweepy.OAuthHandler("OHWsRAyDgzAAdn9Fz2PoJeNo4", "7i39qPfQ71zsR9HYGH6V7wsD0NYvX5waB332aSukHoOsh9xSgM")
    auth.set_access_token("118062980-vgarbjl74jnuT6rXy6SqmfUMExFxPwpUa8aKqYUR", "bYrqvLqm4sW4UQk58ftbhzBVFWSwRaWZy4njpR4Tf38no")
    api = tweepy.API(auth)
    api.update_status (post())

    #time interval for posting the quiz questions
    start_time = datetime.datetime.now()
    interval = start_time + datetime.timedelta(minutes=0.6)

     # dynamically create the interval times
    tweet_times = [start_time.minute, interval.minute]

    while True:
     current_time = datetime.datetime.now()
     if current_time.minute in tweet_times:
        # your function for registeration
        print (LNquiz()) 
        # sleep to avoid running the function again in the next loop
        time.sleep(0.2)  
                
#implementig the AI to parse and read question, pairng with a answer tree
import stanfordcorenlp
          parse(source, filename='question', mode='exec') 