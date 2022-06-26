import pandas as pd
from .trending import *
from datetime import datetime 
import snscrape.modules.twitter as snstwitter 

def scraper(query):
    scraper = snstwitter.TwitterSearchScraper(query).get_items()
    return scraper

def get_tweets(query, limit=10, days_before=None, hours_before=None, minutes_before=None):
    scraper = scraper(query)

    tweets = []
    for i, tweet in enumerate(scraper):
        if days_before is not None:
            if (datetime.now() - tweet.date.replace(tzinfo=None)).days == days_before:
                break
            else:
                tweets.append(tweet.content)
        elif hours_before is not None:
            if (datetime.now() - tweet.date.replace(tzinfo=None)).seconds // 3600 == hours_before:
                break
            else:
                tweets.append(tweet.content)
        elif minutes_before is not None:
            if (datetime.now() - tweet.date.replace(tzinfo=None)).seconds // 60 == minutes_before:
                break
            else:
                tweets.append(tweet.content)
        elif query is None:
            print("Query is None")
            break
        elif (days_before is None) & (hours_before is None) & (minutes_before is None) & (query is not None):
            if i == limit:
                break
            else:
                tweets.append(tweet.content)
        else:
            print("error")
            break

    return tweets


def get_most_trending_tweets(limit=10, days_before=None, hours_before=None, minutes_before=None):
    query = get_most_trending()
    
    scraper = scraper(query)

    tweets = []
    for i, tweet in enumerate(scraper):
        if days_before is not None:
            if (datetime.now() - tweet.date.replace(tzinfo=None)).days == days_before:
                break
            else:
                tweets.append(tweet.content)
        elif hours_before is not None:
            if (datetime.now() - tweet.date.replace(tzinfo=None)).seconds // 3600 == hours_before:
                break
            else:
                tweets.append(tweet.content)
        elif minutes_before is not None:
            if (datetime.now() - tweet.date.replace(tzinfo=None)).seconds // 60 == minutes_before:
                break
            else:
                tweets.append(tweet.content)
        elif query is None:
            print("Query is None")
            break
        elif (days_before is None) & (hours_before is None) & (minutes_before is None) & (query is not None):
            if i == limit:
                break
            else:
                tweets.append(tweet.content)
        else:
            print("error")
            break

    return tweets