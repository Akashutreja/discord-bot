import psycopg2
from datetime import datetime
import os

DATABASE_URL = os.environ['DATABASE_URL']
class Database:
  def __init__(self):
    self.connection = psycopg2.connect(DATABASE_URL, sslmode='require')
    self.create_search_table()

  def create_search_table(self):
    """
    Creates search_history table which stores user search history.
    """
    print("creating table")
    cursor = self.connection.cursor()
    cursor.execute("create table if not exists search_history (user_id VARCHAR(255),search_keyword VARCHAR(255),search_time timestamp);")
    self.connection.commit()

  def post_data(self, user_id, query):
    print("inserting in table")
    cursor = self.connection.cursor()
    cursor.execute("Insert into public.search_history Values('{}', '{}','{}')".format(user_id, query, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    self.connection.commit()

  def fetch_data(self, user_id, query):
    print("fetching from table")
    cursor = self.connection.cursor()
    cursor.execute("Select * from public.search_history where user_id = '{}' and search_keyword like '%".format(user_id) + query +"%'")
    results = cursor.fetchall()
    return results
