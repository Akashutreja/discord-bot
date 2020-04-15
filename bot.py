import discord
from google_search_api import search
from database import post_data, fetch_data, create_search_table
from secret import TOKEN

class MyClient(discord.Client):
    async def on_ready(self):
        print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
        print('Logged on as', self.user)
        create_search_table()

    async def on_message(self, message):
        # don't respond to ourselves
        content = message.content
        if message.author == self.user:
            return

        if content.lower() == 'hey':
            await message.channel.send('hi {}'.format(message.author.mention))
        elif content.startswith('!google'):
          query = message.content.split(None, 1)[1]
          user_id = message.author.id
          post_data(user_id, query)

          results = search(query)
          if results:
            links = ' \n'.join(results)
            bot_message = 'Hey {}, you searched for {}. The top five results are: \n {}'.format(message.author.mention, query, links)
          else:
            bot_message = 'Hey {}, you searched for {}. \n Sorry, no matching links found.'.format(message.author.mention, query)
          await message.channel.send(bot_message)
        elif content.startswith('!recent'):
          query = message.content.split(None, 1)[1]
          user_id = message.author.id
          recent_results = fetch_data(user_id, query)
          if(len(recent_results) > 0):
            bot_message = 'Your matching search results are: \n' + ' \n'.join([data[1] for data in recent_results])
          else: 
              bot_message = 'No matching results found'
          await message.channel.send(bot_message)


client = MyClient() 
client.run(TOKEN)

