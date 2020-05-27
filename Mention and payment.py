import tweepy 
import tippin
from tweepy import OAuthHandler
from tweepy import API
from datetime import datetime, time, timedelta



auth = tweepy.OAuthHandler("OHWsRAyDgzAAdn9Fz2PoJeNo4", "7i39qPfQ71zsR9HYGH6V7wsD0NYvX5waB332aSukHoOsh9xSgM")
auth.set_access_token("118062980-vgarbjl74jnuT6rXy6SqmfUMExFxPwpUa8aKqYUR", "bYrqvLqm4sW4UQk58ftbhzBVFWSwRaWZy4njpR4Tf38no")
api = tweepy.API(auth)
twitterApi = API(auth)

mentions = twitterApi.mentions_timeline(count=1)
now =datetime.now()

for mention in mentions:
     if now < (mention.created_at + timedelta(hours=12 + timedelta(seconds= 10))
        return ("new answers are here")
     else:
        print ("no answers yet")
    #tipin me AP would pay mentions here
    get tipin mention + user ( 'name')
api.update_status (tweet())