#!/usr/bin/python3
""" Module for thats contains the count_words function. """
from requests import get


def count_words(sub_name, search_terms, term_counts=[], next_page=None):
  """
  A function thats :
  Returns the count of the title inputed . 
  """
  user_agent = {'User-Agent': 'HolbertonSchool'}

  lower_terms = [term.lower() for term in search_terms]

  if not term_counts:
    for term in lower_terms:
      term_counts.append(0)

  if next_page is None:
    api_url = 'https://www.reddit.com/r/{}/hot.json'.format(sub_name)
    response = get(api_url, headers=user_agent, allow_redirects=False)
    if response.status_code == 200:
      for post in response.json()['data']['children']:
        term_index = 0
        for term_index in range(len(lower_terms)):
          for word in [w for w in post['data']['title'].split()]:
            word = word.lower()
            if lower_terms[term_index] == word:
              term_counts[term_index] += 1
          term_index += 1

      if response.json()['data']['after'] is not None:
        count_words(sub_name, lower_terms, term_counts, response.json()['data']['after'])
  else:
    api_url = ('https://www.reddit.com/r/{}/hot.json?after={}'
            .format(sub_name, next_page))
    response = get(api_url, headers=user_agent, allow_redirects=False)

    if response.status_code == 200:
      for post in response.json()['data']['children']:
        term_index = 0
        for term_index in range(len(lower_terms)):
          for word in [w for w in post['data']['title'].split()]:
            word = word.lower()
            if lower_terms[term_index] == word:
              term_counts[term_index] += 1
          term_index += 1

      if response.json()['data']['after'] is not None:
        count_words(sub_name, lower_terms, term_counts, response.json()['data']['after'])
      else:
        final_counts = {}
        for key_term in list(set(lower_terms)):
          term_index = lower_terms.index(key_term)
          if term_counts[term_index] != 0:
            final_counts[lower_terms[term_index]] = (term_counts[term_index] *
                                        lower_terms.count(lower_terms[term_index]))

        for term, count in sorted(final_counts.items(),
                                 key=lambda x: (-x[1], x[0])):
          print('{}: {}'.format(term, count))
