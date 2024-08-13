#!/usr/bin/python3
"""Queries the Reddit API, parses the list titles of all the hot
   articles for a given subreddit and prints a sorted count of
   given keywords"""
import requests


def count_words(subreddit, word_list, keyword_count=None, after=None):
    """Prints a sorted count of given keywords"""

    if keyword_count is None:
        keyword_count = {word.lower(): 0 for word in word_list}

    base_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'custom-script/1.0'}
    params = {'limit': 100}
    if after:
        params['after'] = after

    try:
        response = requests.get(base_url, headers=headers,
                                params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            articles = data['data']['children']

            for article in articles:
                title = article['data']['title'].lower().split()

                for word in word_list:
                    keyword_count[word.lower()] += title.count(word.lower())

            after = data['data'].get('after')
            if after is not None:
                return count_words(subreddit, word_list, keyword_count, after)
            else:
                sorted_counts = sorted(
                    [(k, v) for k, v in keyword_count.items() if v > 0],
                    key=lambda item: (-item[1], item[0]),
                )

                for word, count in sorted_counts:
                    print(f"{word}: {count}")
        else:
            return None
    except requests.RequestException:
        return None
