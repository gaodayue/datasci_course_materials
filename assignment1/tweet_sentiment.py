import sys
import json

def build_sentiment_dictionary(sent_file):
    d = {}
    with open(sent_file) as f:
        for line in f:
            term, score = line.split('\t')
            d[term] = int(score)
    return d


def compute_sentiment_score(tweet_str, sent_dict):
    tweet = json.loads(tweet_str)
    if 'text' in tweet:
        return sum(sent_dict.get(word, 0) for word in tweet['text'].split())
    else:
        return 0 # not a status tweet


def main(sent_file, tweet_file):
    sent_dict = build_sentiment_dictionary(sent_file)
    with open(tweet_file) as f:
        for line in f:
            print compute_sentiment_score(line, sent_dict)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
