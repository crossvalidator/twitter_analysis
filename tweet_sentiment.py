import sys
import json 

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
    tweets = []
    for line in tweet_file:
        #print line
        tweet_line = json.loads(line)
        #print tweet_line
        if "text" in tweet_line:
            tweets.append(tweet_line["text"].encode('utf-8'))
    #print tweets
    #print len(tweets)
    #print "aha"
    scores = {}
    for line in sent_file:
        term, score  = line.split("\t")
        scores[term] = float(score)

    
        
    #print "oho"                      
    for item in tweets:
        total = 0.0
        words = []
        words = item.split(" ")
        for everyword in words:
            if everyword in scores:                          
                total += scores[term]
                #print total
        sys.stdout.write(str(total))
        sys.stdout.write("\n")

if __name__ == '__main__':
    main()
