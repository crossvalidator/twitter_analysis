from __future__ import division
import sys
import json


def main():
    tweet_file = open(sys.argv[1])
    tweets = []
    for line in tweet_file:
        
        tweet_line = json.loads(line)
        
        if "text" in tweet_line:
            tweets.append(tweet_line["text"].encode('utf-8'))
    

    frequency_count = {}
    total_count = 0
    for item in tweets:
        words = item.split(" ")
        total_count += len(words)
        for everyword in words:
            if everyword in frequency_count:                          
                frequency_count[everyword] += 1   
            else:
                frequency_count[everyword] = 1
        
        
   
    print total_count
    for k, v in frequency_count.iteritems():
        sys.stdout.write(k + " " + str(v/total_count)) 
        sys.stdout.write("\n") 
         

if __name__ == '__main__':
    main()
