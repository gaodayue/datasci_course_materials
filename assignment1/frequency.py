import sys
import json

def main(tweet_file):
    total_counts = 0
    term_dict = {}
    # process tweets
    with open(tweet_file) as f:
        for line in f:
            tweet = json.loads(line)
            # skip non-status tweets
            if 'text' not in tweet:
                continue
            terms = tweet['text'].split()
            total_counts = total_counts + len(terms)
            # accumulate counts for each term
            for term in terms:
                if term not in term_dict:
                    term_dict[term] = 1
                else:
                    term_dict[term] = term_dict[term] + 1
    # output frequency for each term
    for term, term_count in term_dict.iteritems():
        print '%s %s' % (term.encode('utf-8'), float(term_count) / total_counts)


if __name__ == '__main__':
    main(sys.argv[1])
