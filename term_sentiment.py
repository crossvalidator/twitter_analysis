import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))



def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
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
    
    new_scores = {}
    for item in tweets:
        total = 0.0
        count = 0
        words = []
        words = item.split(" ")
        for everyword in words:
            if everyword in scores:                          
                total += scores[term]
                count += 1
                #print total
        
        if (count == 0):
            continue
        else:
            for everyword in words:
                if everyword not in scores:
                    if everyword in new_scores:
                        #new_scores[everyword][0] += (total/count)
                        new_scores[everyword][0] += total
                        new_scores[everyword][1] += 1
                    else:
                        new_scores[everyword] = [(total/count), 1]
    
    for k, v in new_scores.iteritems():
        sys.stdout.write(k + " " + str(float(v[0]/v[1]))) 
        sys.stdout.write("\n")   

if __name__ == '__main__':
    main()
