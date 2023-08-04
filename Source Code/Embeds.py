# Embeds With Discord.py
# GitHub Source Code
# github.com/Loxingle1

import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
TOKEN = "TOKEN"

@bot.event
async def on_ready():
    print('Logged in as Source Bot#1226.')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Codes"))

# EMBED - TITLE & DESCRIPTION
@bot.command(name="embed_title")
async def embed(ctx):
    embed = discord.Embed(title="Example Embed", description="This is an example embed.")
    await ctx.send(embed=embed)

# EMBED - PROFILE NAME, LINK & IMAGE (AUTHOR)
@bot.command(name="embed_author")
async def embed_author(ctx):
    embed = discord.Embed(title="Example Embed", description="This is an example embed with an author.")
    embed.set_author(name="AtlasL", url="https://github.com/Loxingle1", icon_url="https://i.pinimg.com/originals/e8/a1/53/e8a153c8f4aaa7ce37526149c3f3b621.jpg")
    await ctx.send(embed=embed)

# EMBED - FIELDS & VALUES
@bot.command(name="embed_fields")
async def embed_fields(ctx):
    embed = discord.Embed(title="Example Embed", description="This is an example embed with fields.")
    embed.add_field(name="Embed Field #1", value="Value of Field #1.")
    embed.add_field(name="Embed Field #2", value="Value of Field #2.")
    await ctx.send(embed=embed)

# EMBED - FIELDS & VALUES (INLINE=FALSE)
@bot.command(name="embed_fields2")
async def embed_fields(ctx):
    embed = discord.Embed(title="Example Embed", description="This is an example embed with fields.")
    embed.add_field(name="Embed Field #1", value="Value of Field #1.", inline=False)
    embed.add_field(name="Embed Field #2", value="Value of Field #2.", inline=False)
    await ctx.send(embed=embed)

# EMBED - THUMBNAILS
@bot.command(name="embed_thumbnail")
async def embed_tb(ctx):
    embed = discord.Embed(title="Example Embed", description="This is an example embed with a thumbnail.")
    embed.set_thumbnail(url="https://i.pinimg.com/originals/e8/a1/53/e8a153c8f4aaa7ce37526149c3f3b621.jpg")
    await ctx.send(embed=embed)

# EMBED - COLOURS
@bot.command(name="embed_colour")
async def embed_colour(ctx):
    embed = discord.Embed(title="Example Embed",
                          description="This is an example embed with the colour blue.",
                          color=discord.Color.blue())
    await ctx.send(embed=embed)

# EMBED - IMAGE
@bot.command(name="embed_image")
async def embed_img(ctx):
    embed = discord.Embed(title="Example Embed", description="This is an example embed with an image.")
    embed.set_image(url="https://i.pinimg.com/originals/e8/a1/53/e8a153c8f4aaa7ce37526149c3f3b621.jpg")
    await ctx.send(embed=embed)

# EMBED - COMBINING ALL INTO A SINGLE EMBED
@bot.command(name="embed_all")
async def embed_all(ctx):
    embed = discord.Embed(title="Example Embed",
                          description="This is an example combining all features into one.",
                          color=discord.Color.dark_blue())
    embed.set_author(name="AtlasL", url="https://github.com/Loxingle1", icon_url="https://i.pinimg.com/originals/e8/a1/53/e8a153c8f4aaa7ce37526149c3f3b621.jpg")
    embed.add_field(name="Field #1", value="This is the value of Field #1.", inline=False)
    embed.add_field(name="Field #2", value="This is the value of Field #2", inline=False)
    embed.set_thumbnail(url="https://i.pinimg.com/originals/e8/a1/53/e8a153c8f4aaa7ce37526149c3f3b621.jpg")
    embed.set_image(url="https://i.pinimg.com/originals/e8/a1/53/e8a153c8f4aaa7ce37526149c3f3b621.jpg")
    await ctx.send(embed=embed)

bot.run(TOKEN)