from __future__ import division
from operator import itemgetter
import sys
import json


def main():
    tweet_file = open(sys.argv[1])
    h_tags = []
    for line in tweet_file:
        
        tweet_line = json.loads(line)
        
        if "entities" in tweet_line:
            h_list = tweet_line["entities"]["hashtags"]
            for item in h_list:
                if "text" in item:
                    h_tags.append(item["text"].encode('utf-8'))
            
                

    h_count_dict = {x:float(h_tags.count(x)) for x in h_tags}
    #sorted_h_dict = sorted(h_count_dict.items(), key=itemgetter(1))
    
    count = 0
    top_10_keys = []
    top_10_values = []
    #print len(h_count_dict)
    while count < 10 and count < len(h_count_dict):
        start_count = 0
        for k, v in h_count_dict.iteritems():
            if start_count == 0:
                temp_max_key = k
                temp_max_value = v
                start_count = 1
            
            if v > temp_max_value:
                temp_max_value = v
                temp_max_key = k
        
        sys.stdout.write(temp_max_key + " " + str(temp_max_value))
        sys.stdout.write("\n") 
        del h_count_dict[temp_max_key]
        count += 1
        
        
         

if __name__ == '__main__':
    main()



