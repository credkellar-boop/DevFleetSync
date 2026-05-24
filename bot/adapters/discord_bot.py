import discord
import logging

async def start_discord(token):
    if not token:
        logging.warning("Discord token missing. Skipping Discord setup.")
        return

    # Set up basic intents
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"🟢 Discord Adapter Online: Logged in as {client.user}")

    @client.event
    async def on_message(message):
        # Ignore messages sent by the bot itself
        if message.author == client.user:
            return

        # Basic command listener
        if message.content.startswith('/sync'):
            # TODO: Route this to bot.core.engine
            await message.channel.send("🚀 DevFleetSync (Discord): Syncing your domain...")

    # Start the client
    await client.start(token)
