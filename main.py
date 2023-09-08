import discord


def discord_bot():
    # set up discord bot
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    # the bot is read to use
    @client.event
    async def on_ready():
        print("logged in as {0.user}".format(client))

    # send message
    @client.event
    async def on_message(message):
        print(message)
        print(message.content)
        if message.author == client.user:
            return

        # $meand a command
        if message.content.startswith('$hello'):
            print("message recieved")
            await message.channel.send('hello!')

    # line to run the bot
    bot_token = "MTE0OTcyNzE5MDQxNDUyNDQ4Ng.G7CWrP.FimiSmZLB0eKIQLcTSVQ4gYJN_MMe94skCoef0"
    client.run(bot_token)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    discord_bot()