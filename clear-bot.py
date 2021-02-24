import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print("Bot is online.")

    async def on_message(self, message):
        if message.content.startswith(":clear"):
            if message.author.permissions_in(message.channel).manage_messages:
                args = message.content.split()
                if len(args) == 2:
                    if args[1].isdigit():
                        count = int(args[1]) + 1
                        def is_not_pinned(mess):
                            return not mess.pinned
                        deleted = await message.channel.purge(limit=count, check=is_not_pinned)
                        await message.channel.send('{} messages deleted.'.format(len(deleted) - 1))