import requests
from googlesearch import search

def search_data(query='food'):
  """
  To fetch top 5 links from google for particular keyword
  Input:
  query: keyword for which we want top 5 google links
  """
  result = []
  for links in search(query, tld="co.in", num=10, stop=5, pause=2):
    result.append(links)
  return result