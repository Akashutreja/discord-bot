import psycopg2
from secret import db_host,db_port,db_name,db_user,db_password
from datetime import datetime

def create_connection():
  connection = psycopg2.connect(host=db_host, 
    port=db_port, 
    user=db_user, 
    password=db_password,
    database=db_name, 
    sslmode='require')
  return connection

def create_search_table():
  """
  Creates search_history table which stores user search history .
  """
  connection = create_connection()
  cursor = connection.cursor()
  cursor.execute("create table if not exists search_history (user_id VARCHAR(255),search_keyword VARCHAR(255),search_time timestamp);")
  connection.commit()
  connection.close()

def post_data(user_id, query):
  connection = create_connection()
  cursor = connection.cursor()
  cursor.execute("Insert into public.search_history Values('{}', '{}','{}')".format(user_id, query, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
  connection.commit() 
  connection.close()

def fetch_data(user_id, query):
  connection = create_connection()
  cursor = connection.cursor()
  cursor.execute("Select * from public.search_history where user_id = '{}' and search_keyword like '%".format(user_id) + query +"%'")
  results = cursor.fetchall()
  connection.close()
  return results
