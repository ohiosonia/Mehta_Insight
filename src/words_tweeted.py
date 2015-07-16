# example of program that calculates the total number of times each word has been tweeted.
import csv
import re
import sys
from collections import Counter


tweets =  sys.stdin

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

print sys.argv

# print word_counts
# with open('txt.txt','wb') as f:
#     w = csv.writer(f)
#     w.writerows(sorted(word_counts.items()))

# cat tweet_input/tweets.txt | python src/words_tweeted.py ft1.txt