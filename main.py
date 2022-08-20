import os
import discord
from dotenv import load_dotenv
from code_challenge import Challenge
from enums import Difficulty

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

active_challenges = {}

@client.event
async def on_ready():
    print(f"Logged on as {client.user}!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")

    if message.content.startswith("$new"):
        if active_challenges.get(message.guild.id):
            await message.channel.send("Error: Challenge already active in this server.")
            return

        challenge = Challenge(Difficulty.EASY, "add_two")

        active_challenges[message.guild.id] = challenge

        ret_msg = f"""
        New challenge started!
**Name:** {challenge.challenge_name_display}
**Description:**  {challenge.description}
**Template:**
```py
{challenge.template}
```
        """

        await message.channel.send(ret_msg)

    if message.content.startswith("$delete"):
        if not active_challenges.get(message.guild.id):
            await message.channel.send("Error: No active challenge in this server.")
            return

        del active_challenges[message.guild.id]
        await message.channel.send("Active challenge has been removed.")

    if message.content.startswith("$attempt"):
        active_challenge = active_challenges.get(message.guild.id)

        if not active_challenge:
            await message.channel.send("Error: No active challenge in this server.")
            return

        code_list = message.content.split("```")[1].split("\n")[1:]
        parsed_code = "\n".join(code_list)

        result = active_challenge.execute_attempt(parsed_code)

        await message.channel.send(result.message)


client.run(os.getenv("DISCORD_TOKEN"))
