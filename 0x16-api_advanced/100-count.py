#!/usr/bin/python3
""" Module for thats containes count_occurrences function. """
from requests import get


def count_occurrences(subreddit_id, search_terms, occurrences=[], next_page=None):
    """
    Return the count of title inputed.
    """
    headers = {'User-Agent': 'HolbertonSchool'}

    search_terms = [term.lower() for term in search_terms]

    if not bool(occurrences) is False:
        for term in search_terms:
            occurrences.append(0)

    if next_page is None:
        endpoint = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit_id)
        response = get(endpoint, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            for post in response.json()['data']['children']:
                idx = 0
                for idx in range(len(search_terms)):
                    for term in [t for t in post['data']['title'].split()]:
                        term = term.lower()
                        if search_terms[idx] == term:
                            occurrences[idx] += 1
                    idx += 1

            if response.json()['data']['after'] is not None:
                count_occurrences(subreddit_id, search_terms,
                                  occurrences, response.json()['data']['after'])
    else:
        endpoint = ('https://www.reddit.com/r/{}/hot.json?after={}'
                    .format(subreddit_id,
                            next_page))
        response = get(endpoint, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            for post in response.json()['data']['children']:
                idx = 0
                for idx in range(len(search_terms)):
                    for term in [t for t in post['data']['title'].split()]:
                        term = term.lower()
                        if search_terms[idx] == term:
                            occurrences[idx] += 1
                    idx += 1
            if response.json()['data']['after'] is not None:
                count_occurrences(subreddit_id, search_terms,
                                  occurrences, response.json()['data']['after'])
            else:
                result_counts = {}
                for term in list(set(search_terms)):
                    idx = search_terms.index(term)
                    if occurrences[idx] != 0:
                        result_counts[search_terms[idx]] = (occurrences[idx] *
                                                             search_terms.count(search_terms[idx]))

                for term, count in sorted(result_counts.items(),
                                          key=lambda x: (-x[1], x[0])):
                    print('{}: {}'.format(term, count))

