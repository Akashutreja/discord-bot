import requests
from googlesearch import search

def search(query='food'):
  result = []
  for links in search(query, tld="co.in", num=10, stop=5, pause=2):
    result.append(links)
  return result