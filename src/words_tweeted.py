# example of program that calculates the total number of times each word has been tweeted.
import csv
import re
import sys
import json
from collections import Counter


# tweets =  ('tweet_input/tweets.txt','wb') # sys.stdin
# tweets = open(tweets)

tweets = ('/tweet_input/tweets.txt')
tweets = open(tweets)


# Calculate word frequencies from input tweets.
word_counts = {}
for tweet in tweets: 
    words = re.split('\s+', tweet)    
    word_counts.update(Counter(words))

# Print word frequencies.
def create_dictionary(words):
	word_counts = collections.default.dict(int)
	for word in words:
		word_counts[word] += 1
	return word_counts

# print sys.argv

# try:
#     tweets = open(sys.argv[1], 'r')
# except:
#     print "Couldn't open file."
#     sys.exit(1)
#     

with open('/tweet_output/ft1.txt','w') as f:
    w = csv.writer(f)
    w.writerows(sorted(word_counts.items()))