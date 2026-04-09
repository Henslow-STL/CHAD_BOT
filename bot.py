import os
import discord
from discord import app_commands
from dotenv import load_dotenv

from weather_service import get_weather_data, compare_weather, cities

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@client.event
async def on_ready():
    await tree.sync()
    print(f"Logged in as {client.user}")


@tree.command(name="weather", description="Compare weather between cities")
async def weather(interaction: discord.Interaction):
    await interaction.response.defer()

    results = []

    for city in cities:
        data = get_weather_data(city["name"], city["lat"], city["lon"])
        if data is not None:
            results.append(data)

    if len(results) < 2:
        await interaction.followup.send("Error retrieving weather data.")
        return

    city1, city2 = results
    comparison = compare_weather(city1, city2)

    message = (
    f"**Chad's Weather Report**\n\n"
    f"**{city1['city']}**\n"
    f"Current Temp: {city1['temperature']:.1f}°F\n"
    f"Conditions: {city1['description']}\n"
    f"Humidity: {city1['humidity']}%\n"
    f"High: {city1['high']:.1f}°F\n"
    f"Low: {city1['low']:.1f}°F\n"
    f"Chance of Rain: {city1['rain_chance']}%\n"
    f"Alert: {city1['alert']}\n\n"
    f"**{city2['city']}**\n"
    f"Current Temp: {city2['temperature']:.1f}°F\n"
    f"Conditions: {city2['description']}\n"
    f"Humidity: {city2['humidity']}%\n"
    f"High: {city2['high']:.1f}°F\n"
    f"Low: {city2['low']:.1f}°F\n"
    f"Chance of Rain: {city2['rain_chance']}%\n"
    f"Alert: {city2['alert']}\n"
    )

    await interaction.followup.send(message)


client.run(TOKEN)