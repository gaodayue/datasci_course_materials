import sys
import json

def build_sentiment_dictionary(sent_file):
    d = {}
    with open(sent_file) as f:
        for line in f:
            term, score = line.split('\t')
            d[term] = int(score)
    return d


def main(sent_file, tweet_file):
    sent_dict = build_sentiment_dictionary(sent_file)
    newterm_dict = {}
    # process tweets
    with open(tweet_file) as f:
        for line in f:
            tweet = json.loads(line)
            # skip non-status tweets
            if 'text' not in tweet:
                continue
            tweet_score = sum(sent_dict.get(word, 0) for word in tweet['text'].split())
            # collect new terms
            for term in tweet['text'].split():
                if term not in sent_dict:
                    newterm_dict.setdefault(term, []).append(tweet_score)
    # output score for new term
    for term, scores in newterm_dict.iteritems():
        print '%s %s' % (term.encode('utf-8'), float(sum(scores)) / len(scores))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
