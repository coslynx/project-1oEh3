```python
# scheduled_messages.py

import discord
from discord.ext import commands
import asyncio

class ScheduledMessages(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='schedule_message')
    async def schedule_message(self, ctx, channel: discord.TextChannel, time, *, message):
        try:
            await channel.send(f"Message scheduled for {time}: {message}")
            await asyncio.sleep(time)  # Sleep for the specified time
            await channel.send(message)
        except Exception as e:
            print(f"An error occurred: {e}")

def setup(bot):
    bot.add_cog(ScheduledMessages(bot))
```
In this file, we create a Discord cog for handling scheduled messages. The `schedule_message` function allows users to schedule a message to be sent in a specific channel at a specified time. The message is initially sent confirming the scheduling, and then after the specified time has elapsed, the actual message is sent to the channel. The function includes error handling to catch and print any exceptions that may occur during the process.