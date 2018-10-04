import json
import re
import pandas as pd
import matplotlib.pyplot as plt


# Return True if a word is found in text, otherwise it returns False.
def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    return True if match else False


# Use regular expressions for retrieving link that start with "http://" or
# "https://" from a text.
# Return the url if found, otherwise it returns an empty string.
def extract_link(text):
    regex = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
    match = re.search(regex, text)
    if match:
        return match.group()
    return ''


if __name__ == "__main__":
    # Read the data in into an array that we call tweets.
    tweets_data_path = 'data/twitter_data.txt'
    tweets_file = open(tweets_data_path, "r")

    tweets_data = []
    for line in tweets_file:
        try:
            tweet = json.loads(line)
            tweets_data.append(tweet)
        except:
            continue

    # Create an empty DataFrame called tweets.
    tweets = pd.DataFrame()

    #  Add text column to the tweets DataFrame, which contains the tweet.
    tweets['text'] = list(map(lambda tweet: tweet['text'], tweets_data))

    # Add 3 more columns.
    tweets['python'] = tweets['text'].apply(lambda tweet: word_in_text('python', tweet))
    tweets['javascript'] = tweets['text'].apply(lambda tweet: word_in_text('javascript', tweet))
    tweets['ruby'] = tweets['text'].apply(lambda tweet: word_in_text('ruby', tweet))

    # We are interested in targetting tweets that are related to programming
    # languages, i.e. contains "programming" or "tutorial".
    tweets['programming'] = tweets['text'].apply(lambda tweet: word_in_text('programming', tweet))
    tweets['tutorial'] = tweets['text'].apply(lambda tweet: word_in_text('tutorial', tweet))

    # Relevant if contains the word "programming" or "tutorial".
    tweets['relevant'] = tweets['text'].apply(lambda tweet: word_in_text('programming', tweet) or word_in_text('tutorial', tweet))

    # Contain the urls information.
    tweets['link'] = tweets['text'].apply(lambda tweet: extract_link(tweet))

    # Create a new DataFrame called tweets_relevant_with_link. This DataFrame
    # is a subset of tweets DataFrame and contains all relevant tweets that
    # have a link.
    tweets_relevant = tweets[tweets['relevant'] == True]
    tweets_relevant_with_link = tweets_relevant[tweets_relevant['link'] != '']

    # Print out all Python-related, Javascript-related, Ruby-related links.
    tweets_python = tweets_relevant_with_link[tweets_relevant_with_link['python'] == True]
    tweets_javascript = tweets_relevant_with_link[tweets_relevant_with_link['javascript'] == True]
    tweets_ruby = tweets_relevant_with_link[tweets_relevant_with_link['ruby'] == True]

    python_links = tweets_python['link']
    javascript_links = tweets_javascript['link']
    ruby_links = tweets_ruby['link']

    print("PYTHON LINKS")
    print("------------")
    for link in python_links:
        print(link)
    print()

    print("JAVASCRIPT LINKS")
    print("----------------")
    for link in javascript_links:
        print(link)
    print()

    print("RUBY LINKS")
    print("----------")
    for link in ruby_links:
        print(link)