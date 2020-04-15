import requests
import json
GOOGLE_SEARCH_API_KEY = 'AIzaSyDgdNn-szqB9Fl9iREjr3Fctd_NuDmiA_o'
CX_ID = '017015570155260285259:k3m865zaiuk'


def search(query):
  URL = 'https://www.googleapis.com/customsearch/v1?key={}&cx={}&q={}'.format(GOOGLE_SEARCH_API_KEY,CX_ID,query)
  content = requests.get(URL)
  json_data = json.loads(content.text)
  result = []
  for value in json_data['items']:
    result.append(value['link'])
  top_links = min(5,len(result))
  return result[:top_links]