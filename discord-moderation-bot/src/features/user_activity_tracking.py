```python
# user_activity_tracking.py

import discord
from datetime import datetime

class UserActivityTracking:
    def __init__(self, client):
        self.client = client
        self.user_activity_data = {}

    async def track_user_activity(self, message):
        author_id = str(message.author.id)
        if author_id not in self.user_activity_data:
            self.user_activity_data[author_id] = {
                'message_count': 0,
                'join_date': str(message.author.joined_at),
                'last_active_date': str(datetime.now())
            }
        self.user_activity_data[author_id]['message_count'] += 1
        self.user_activity_data[author_id]['last_active_date'] = str(datetime.now())

    async def get_user_activity(self, user_id):
        user_id = str(user_id)
        if user_id in self.user_activity_data:
            return self.user_activity_data[user_id]
        else:
            return None

    async def clear_user_activity_data(self, user_id):
        user_id = str(user_id)
        if user_id in self.user_activity_data:
            del self.user_activity_data[user_id]

    async def display_user_activity(self, ctx, user_id):
        user_activity = await self.get_user_activity(user_id)
        if user_activity:
            await ctx.send(f"User {user_id} activity data:\nMessage Count: {user_activity['message_count']}\nJoin Date: {user_activity['join_date']}\nLast Active Date: {user_activity['last_active_date']}")
        else:
            await ctx.send("User activity data not found.")

    async def on_message(self, message):
        await self.track_user_activity(message)

    async def on_member_join(self, member):
        author_id = str(member.id)
        if author_id not in self.user_activity_data:
            self.user_activity_data[author_id] = {
                'message_count': 0,
                'join_date': str(member.joined_at),
                'last_active_date': str(datetime.now())
            }
```
This code provides a class `UserActivityTracking` that tracks user activity in a Discord server. It includes methods to track message count, join date, and last active date for each user. The class also includes methods to retrieve, clear, and display user activity data. The `on_message` and `on_member_join` methods are used as event handlers to update user activity data when messages are sent or when new members join the server.