import psycopg2
from datetime import datetime
import os

class Database:
  def __init__(self):
    self.connection = psycopg2.connect(os.environ['DATABASE_URL'], sslmode='require')
    self.create_search_table()

  def create_search_table(self):
    """
    Creates search_history table which stores user search history.
    """
    cursor = self.connection.cursor()
    cursor.execute("create table if not exists search_history (user_id VARCHAR(255),search_keyword VARCHAR(255),search_time timestamp);")
    self.connection.commit()

  def post_data(self, user_id, query):
    """
    Store data in serach_history table
    Inputs:
    user_id: user id who is doing chat
    query:   keyword that user is seraching like !google kewyword 
    """
    try:
      cursor = self.connection.cursor()
      cursor.execute("Insert into public.search_history Values('{}', '{}','{}')".format(user_id, query, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
      self.connection.commit()
    except Exception as e:
      self.connection.rollback()
      print("exception")
      raise e

  def fetch_data(self, user_id, query):
    """
    Fetch data from serach_history to get history of particular user for a particular keyword
    Inputs:
    user_id: user id who is requesting search history
    query:   keyword for which user is asking history like !recent keyword
    """
    try:
      cursor = self.connection.cursor()
      cursor.execute("Select * from public.search_history where user_id = '{}' and search_keyword like '%".format(user_id) + query +"%'")
      results = cursor.fetchall()
      return results
    except Exception as e:
      print("exception")
      self.connection.rollback()