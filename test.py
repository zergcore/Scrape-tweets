#snscrape --jsonl --progress --max-results 500 twitter-search "from:sasha35625 until:2022-07-26 since:2022-01-01 filter:replies" > text-query-tweets.json
#snscrape --jsonl --progress --max-results 10000 twitter-search "to:sasha35625 @sasha35625 min_replies:1 until:2022-06-26 since:2022-01-01" > text-query-tweets.json

import os
import pandas as pd

# Using OS library to call CLI commands in Python
#os.system("snscrape --jsonl --progress --max-results 20000 twitter-search \"to:sasha35625 since:2022-01-01\" > text-query-tweets.json")

# Reads the json generated from the CLI commands above and creates a pandas dataframe
tweets_df = pd.read_json('text-query-tweets.json', lines=True)
print(tweets_df)
tweets_df.pop('_type')
tweets_df.pop('renderedContent')
tweets_df.pop('id')
tweets_df.pop('source')
tweets_df.pop('sourceUrl')
tweets_df.pop('sourceLabel')
tweets_df.pop('outlinks')
tweets_df.pop('tcooutlinks')
tweets_df.pop('retweetedTweet')
tweets_df.pop('cashtags')
tweets_df.pop('hashtags')
tweets_df.pop('place')
tweets_df.pop('coordinates')
tweets_df.pop('mentionedUsers')
tweets_df.pop('inReplyToTweetId')
print(tweets_df)

tweets_df.to_csv('sashas_tweets.csv', encoding='utf-8', index=False)