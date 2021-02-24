import discord

description = 'You wanted to wrote an suggest but you wrote it wrong.\nThe suggest-message need 3 parts: a title, an idea and a reason\nHere is an example: :suggest title idea reason channel \nWrite the channel with `#` .\nYou want me on your Server? Invite me: https://discord.com/api/oauth2/authorize?client_id=813351259930099773&permissions=54525137&scope=bot'

client = discord.Client()


class MyClient(discord.Client):
    async def on_ready(self):
        print("Bot is online")
        
        await client.change_presence(activity=discord.Game(':suggest; Vorschläge ich komme!'))

    async def on_message(self, message):
      if str(message.author) == client.User:
        return

      if message.content.startswith(":suggest"):

        d_embed = discord.Embed(
          title="Invalid Suggest",
          colour=discord.Colour(0xf1fb21)
        )

        d_embed.set_author(name="Suggest Bot", icon_url="https://cdn.discordapp.com/attachments/813350910355832864/813705594447855667/light-bulb-2010022.jpg")
        d_embed.set_footer(text="Suggest Bot made by xilef601.")

        d_embed.add_field(name="**Description**", value=description)
        d_embed.add_field(name="**Version**", value=version)

        try:
          title = message.content.split("+")[1].replace('+', '')
        except:
          await message.author.send(embed=d_embed)
          return
        try:
          idea = message.content.split("+")[2].replace('+', '')
        except:
          await message.author.send(embed=d_embed)
          return
        try:
          reason = message.content.split("+")[3].replace('+', '')
        except:
          reason = "No reason given!"
        try:
          author = str(message.author)
        except:
          await message.author.send(embed=d_embed)
          return
        try:
          channel_name = message.content.split("+")[4].replace('+', '')
        except:
          pass

        s_channel = discord.utils.get(message.guild.channels, name=str(channel_name))

        if title == "":
          await message.author.send(embed=d_embed)
          return
        elif idea == "":
          await message.author.send(embed=d_embed)
          return
        elif reason == "":
          return

        s_embed = discord.Embed(
          title=title,
          colour=discord.Colour(0xf1fb21)
        )

        s_embed.set_author(name="**" + author + "**")
        s_embed.set_footer(text="Suggest Bot made by xilef601.")

        s_embed.add_field(name="**IDEA**", value=idea)
        s_embed.add_field(name="**REASON**", value=reason)

        
        if channel_name.startswith('<'):
          channel_name_ = channel_name.replace('<', '')
          channel_name = channel_name_.replace('#', '')
          channel_name_ = channel_name.replace('>', '')
          s_id_channel = client.get_channel(int(channel_name_))
          await s_id_channel.send(embed=s_embed)
        else:
          await channel_name.send(embed=s_embed)

      if message.content.startswith(":help"):

        h_embed = discord.Embed(
          title="Invalid Suggest",
          colour=discord.Colour(0xf1fb21)
        )

        h_embed.set_author(name="Suggest Bot", icon_url="https://cdn.discordapp.com/attachments/813350910355832864/813705594447855667/light-bulb-2010022.jpg")
        h_embed.set_footer(text="Suggest Bot made by xilef601.")

        h_embed.add_field(name="**Description**", value=description)


        await message.author.send(embed=h_embed)

client = MyClient()
client.run("Your Token")