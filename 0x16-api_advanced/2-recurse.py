#!/usr/bin/python3
"""Queries the Reddit API and returns the list titles of all the hot
   articles for a given subreddit"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Prints the titles of articles"""

    if hot_list is None:
        hot_list = []

    base_url = f"https://www.reddit.com/r/{subreddit}/hot.json?"
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
            if not articles:
                return hot_list

            hot_list.extend(article['data']['title'] for article in articles)

            after = data['data'].get('after')
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except requests.RequestException:
        return None
