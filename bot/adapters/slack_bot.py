import logging
from slack_bolt.async_app import AsyncApp
from slack_bolt.adapter.socket_mode.async_handler import AsyncSocketModeHandler

async def start_slack(bot_token, app_token):
    if not bot_token or not app_token:
        logging.warning("Slack tokens missing. Skipping Slack setup.")
        return

    # Initialize the async app
    app = AsyncApp(token=bot_token)

    # Listen for messages containing "sync"
    @app.message("sync")
    async def handle_sync_message(message, say):
        # TODO: Route this to bot.core.engine
        await say("🚀 DevFleetSync (Slack): Syncing your domain...")

    print("🟢 Slack Adapter Online.")
    
    # Start the Socket Mode handler asynchronously
    handler = AsyncSocketModeHandler(app, app_token)
    await handler.start_async()
