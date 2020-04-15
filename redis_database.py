from datetime import timedelta
import json
import redis

class RedisDatabase:
  def __init__(self):
    self.redis_conn = redis.from_url(os.environ.get("REDIS_URL"))
    print("intializeing connection")

  def post_data(self, query, value):
    json_dump_value = json.dumps(value)
    self.redis_conn.setex(query, timedelta(minutes=1),json_dump_value)
    print("posted data in redis")

  def fetch_data(self, query):
    json.loads(self.redis_conn.get(query))
    print("fetch from redis done")

  def key_exists(self, query):
    return self.redis_conn.exists(query)