import bs4
import requests
from googlesearch import search



def search_result(query='food'):
  result = ''
  for j in search(query, tld="co.in", num=10, stop=5, pause=2):
    result = result+j+"\n"
  return result
# def search_result(query='test'):
#   result = []
#   for j in search(query, tld="co.in", num=10, stop=5, pause=2):
#     print(j)
#     # result = result+j+'/n'
#     # return result

print(search_result('zkclq'))