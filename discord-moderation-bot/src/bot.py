```python
# bot.py

import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

from commands import custom_commands, moderation_commands, role_commands
from features import anti_spam, logging, scheduled_messages, user_verification, user_activity_tracking, customizable_responses, vote_kick_system
from enhancements import machine_learning, user_reputation_system, user_feedback, dashboard
from utils import config, constants, helpers

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

# Add command modules
bot.add_cog(custom_commands.CustomCommands(bot))
bot.add_cog(moderation_commands.ModerationCommands(bot))
bot.add_cog(role_commands.RoleCommands(bot))

# Add feature modules
anti_spam.setup(bot)
logging.setup(bot)
scheduled_messages.setup(bot)
user_verification.setup(bot)
user_activity_tracking.setup(bot)
customizable_responses.setup(bot)
vote_kick_system.setup(bot)

# Add enhancement modules
machine_learning.setup(bot)
user_reputation_system.setup(bot)
user_feedback.setup(bot)
dashboard.setup(bot)

bot.run(TOKEN)
```