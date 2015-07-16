# example of program that calculates the total number of times each word has been tweeted.
import csv
import re
import sys
from collections import Counter

tweets = ('/Users/soniamehta/Desktop/cc-example/tweet_input/tweets.txt')
tweets = open(tweets)


# Calculate word frequencies from input tweets.
word_counts = {}
for tweet in tweets: #sys.stdin:
    words = re.split('\s+', tweet)    
    word_counts.update(Counter(words))

# Print word frequencies.
for key in sorted(word_counts.keys()):  # iterate through sorted dictionary
    a =  [key, word_counts[key]]
    print a

with open("output.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(a)