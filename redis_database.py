from datetime import timedelta
import json
import redis
import os

class RedisDatabase:
  def __init__(self):
    self.redis_conn = redis.from_url(os.environ.get("REDIS_URL"))

  def post_data(self, query, value):
    """
    Store results from google in redis cache with expiry time of 1 minute
    Inputs:
    query: keyword that user is searching
    value: links corresponing to that keyword from google
    """
    json_dump_value = json.dumps(value)
    self.redis_conn.setex(query, timedelta(minutes=1),json_dump_value)

  def fetch_data(self, query):
    """
    Fetch data from redis cache for particular keyword
    Input:
    query: keyword for which user want google links
    """
    return json.loads(self.redis_conn.get(query))

  def key_exists(self, query):
    """
    Check if particular key exist in redis cache or not
    Input:
    query: key for reids cache
    """
    return self.redis_conn.exists(query)