from google_search import search_data
from  redis_database import RedisDatabase
from database import Database
import discord
import os

class MyClient(discord.Client):

    async def on_ready(self):
        print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
        print('Logged on as', self.user)
        self.redis_db = RedisDatabase()
        self.db = Database()

    async def on_message(self, message):
        # don't respond to itself
        content = message.content
        if message.author == self.user:
            return

        if content.lower() == 'hey':
            await message.channel.send('hi {}'.format(message.author.mention))
        elif content.startswith('!google'):
          query = message.content.split(None, 1)
          if len(query)>1:
            query_to_search = query[1]
            user_id = message.author.id
            self.db.post_data(user_id, query_to_search)

            #fetch from redis
            if self.redis_db.key_exists(query_to_search):
              results = self.redis_db.fetch_data(query_to_search)
            else:
              results = search_data(query_to_search)
              self.redis_db.post_data(query_to_search, results)

            #prepare bot message
            if results:
              links = ' \n'.join(results)
              bot_message = 'Hey {}, you searched for {}. The top five results are: \n {}'.format(message.author.mention, query_to_search, links)
            else:
              bot_message = 'Hey {}, you searched for {}. \n Sorry, no matching links found.'.format(message.author.mention, query_to_search)
          else:
            bot_message = 'Hey {}, please search like "!google query" to get top results from google'.format(message.author.mention)
          await message.channel.send(bot_message)
        elif content.startswith('!recent'):
          query = message.content.split(None, 1)
          if len(query)>1:
            query_to_fetch = query[1]
            user_id = message.author.id
            recent_results = self.db.fetch_data(user_id, query_to_fetch)
            if(len(recent_results) > 0):
              bot_message = 'Your matching search results are: \n' + ' \n'.join([data[1] for data in recent_results])
            else: 
                bot_message = 'No matching results found'
          else:
            bot_message = 'To get search history use command "recent! query"'
          await message.channel.send(bot_message)


client = MyClient()
TOKEN = os.environ['TOKEN']
client.run(TOKEN)

