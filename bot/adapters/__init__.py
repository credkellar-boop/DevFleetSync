# Expose the start functions to the rest of the bot
from .discord_bot import start_discord
from .telegram_bot import start_telegram
from .slack_bot import start_slack

__all__ = ["start_discord", "start_telegram", "start_slack"]
