# example of program that captures 'running' median of tweets
import numpy as np

tweets = open('/tweet_input/tweets.txt')
results = open('/tweet_output/ft2.txt','w')

length_tweet = []

# Get all words
def all_words(word_list):
    word_count = {}
    for word in word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return len(word_count)
    
# Get total words
for line in iter(tweets):
     words =  line.split(' ',len(line)-1)
     length_tweet.append(all_words(words))

# Print median
for l in range(len(length_tweet)):
    results.write('%.3f\n'%np.median(length_tweet[0:l+1]))
