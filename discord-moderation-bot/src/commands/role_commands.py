```python
# File: role_commands.py

import discord
from discord.ext import commands

class RoleCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='add_role')
    async def add_role(self, ctx, member: discord.Member, role: discord.Role):
        try:
            await member.add_roles(role)
            await ctx.send(f"Role {role.name} added to {member.display_name}.")
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")

    @commands.command(name='remove_role')
    async def remove_role(self, ctx, member: discord.Member, role: discord.Role):
        try:
            await member.remove_roles(role)
            await ctx.send(f"Role {role.name} removed from {member.display_name}.")
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")

    @commands.command(name='list_roles')
    async def list_roles(self, ctx, member: discord.Member):
        roles = member.roles
        role_names = [role.name for role in roles]
        await ctx.send(f"Roles of {member.display_name}: {', '.join(role_names)}")

def setup(bot):
    bot.add_cog(RoleCommands(bot))
```
The `role_commands.py` file contains commands related to role management in the Discord server. It includes functions to add, remove, and list roles for a specific member. Each function has error handling to ensure smooth operation.