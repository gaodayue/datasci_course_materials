import sys
import json

def main(tweet_file):
    hashtag_dict = {}
    # process tweets
    with open(tweet_file) as f:
        for line in f:
            tweet = json.loads(line)
            for tag in tweet.get('entities', {}).get('hashtags', []):
                tagtext = tag['text']
                if tagtext not in hashtag_dict:
                    hashtag_dict[tagtext] = 1
                else:
                    hashtag_dict[tagtext] += 1

    sorted_tags = sorted(hashtag_dict.items(), key=lambda x: x[1], reverse=True)
    # output top ten hashtags
    for tag, count in sorted_tags[:10]:
        print '%s %s' % (tag.encode('utf-8'), count)


if __name__ == '__main__':
    main(sys.argv[1])
