import pandas as pd
import snscrape.modules.twitter as snstwitter 

def get_trending():
    scraper = snstwitter.TwitterTrendsScraper()
    scraper_items = scraper.get_items()

    trends = []

    for i, trend in enumerate(scraper_items):
        trend_context = trend.domainContext
        trend_name = trend.name
        trend_count = trend.metaDescription

        try:
            trend_count = trend_count.split(" ")[0]
            if 'M' in trend_count:
                trend_count = int(float(trend_count[:-1])*1000000)
            elif 'K' in trend_count:
                trend_count = int(float(trend_count[:-1])*1000)
            elif ',' in trend_count:
                trend_count = int(trend_count.replace(",", ""))
            else:
                trend_count = int(trend_count)
        except:
            trend_count = 0

        trend_item = {'context': trend_context, 'name': trend_name, 'counts': trend_count, 'url': trend}
        trends.append(trend_item)

    df_trends = pd.DataFrame(trends).sort_values('counts', ascending=False).reset_index(drop=True)
    return df_trends

def get_trending_by_id(id):
    pass

def get_trending_by_name(name):
    pass

def get_most_trending():
    trends = get_trending()
    return trends['name'][0]
