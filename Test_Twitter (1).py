import pandas as pd
!pip install pymongo
from pymongo import MongoClient
import snscrape.modules.twitter as Sntwitter

client = MongoClient("mongodb://localhost:27017/")
db = client["twitter_db"]
collection = db["tweets"]

keyword = input("Enter keyword or hashtag to search: ")
start_date = input("Enter start date (yyyy-mm-dd): ")
end_date = input("Enter end date (yyyy-mm-dd): ")
Enter
keyword or hashtag
to
search: python
Enter
start
date(yyyy - mm - dd): 2023 - 04 - 01
Enter
end
date(yyyy - mm - dd): 2023 - 04 - 0
8
limit = int(input("Enter number of tweets to be scraped: "))
Enter
number
of
tweets
to
be
scraped: 100
query = f"{keyword} since:{start_date} until:{end_date}"

tweets_list = []
for i, tweet in enumerate(Sntwitter.TwitterSearchScraper(query).get_items()):
    if i >= limit:
        break
    tweets_list.append({
        "date": tweet.date,
        "id": tweet.id,
        "url": tweet.url,
        "content": tweet.content,
        "user": tweet.user.username,
        "reply_count": tweet.replyCount,
        "retweet_count": tweet.retweetCount,
        "language": tweet.lang,
        "source": tweet.sourceLabel,
        "like_count": tweet.likeCount
    })
tweets_df = pd.DataFrame(tweets_list,
                         columns=['date', 'id', 'url', 'content', 'user', 'reply_count', 'retweet_count', 'language',
                                  'source', 'like_count'])
document = {"Scraped Word": keyword, "Scraped Date": start_date, "Scraped Data": tweets_df.to_dict("records")}
collection.insert_one(document)

!pip
install
streamlit
import streamlit as st

st.set_option("deprecation.showfileUploaderEncoding", False)
st.set_page_config(page_title="Twitter Scraper", page_icon=":bird:")


def app():
    st.sidebar.subheader("Twitter Search")
    keyword = st.sidebar.text_input("Keyword or hashtag")
    start_date = st.sidebar.date_input("Start date")
    end_date = st.sidebar.date_input("End date")
    limit = st.sidebar.number_input("Limit", value=100, min_value=1, max_value=1000)


if st.sidebar.button("Search"):
    tweets_list = []
    for i, tweet in enumerate(
            sntwitter.TwitterSearchScraper(f'{keyword} since:{start_date} until:{end_date}').get_items()):
        if i >= limit:
            break
        tweets_list.append(
            [tweet.date, tweet.id, tweet.url, tweet.content, tweet.user.username, tweet.replyCount, tweet.retweetCount,
             tweet.lang, tweet.sourceLabel, tweet.likeCount])
    tweets_df = pd.DataFrame(tweets_list,
                             columns=['date', 'id', 'url', 'content', 'user', 'reply_count', 'retweet_count',
                                      'language', 'source', 'like_count'])
2023 - 04 - 0
8
13: 45:05.628

if st.button("Upload to MongoDB"):
    document = {"Scraped Word": keyword, "Scraped Date": start_date, "Scraped Data": tweets_df.to_dict("records")}
    collection.insert_one(document)
    st.success("Data uploaded to MongoDB")
if st.button("Download CSV"):
    tweets_df.to_csv("tweets.csv")




