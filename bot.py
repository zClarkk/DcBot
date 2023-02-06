# bot.py
import os
import random
import discord
import json
import asyncio
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()
bot = commands.Bot(command_prefix='!') # prefix for bot commands

@bot.command(name='flag', help='Posts an image of a flag and has you guess the country')
async def flag(ctx):
    global tmp
    # This is a mistake. Don't do this.
    countries = ['Afghanistan','Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Antarctica',
                    'Antigua and Barbuda','Argentina','Aruba','Australia','Austria','Azerbaijan','Bahamas','Bahrain','Bangladesh','Barbados','Belarus','Belgium','Belize','Benin','Bermuda',
                    'Bhutan','Bolivia','Bosnia','Botswana','Brazil','Brunei','Bulgaria','Burkina Faso','Burundi','Cabo Verde','Cambodia','Cameron','Canada','Caribbean Netherlands',
                    'Central African Republic','Chile','China','Christmas Island','Colombia','Comoros','Congo','Costa Rica','Croatia','Cuba',
                    'Cyprus','Czechia','Denmark','Djibouti','Dominica','Dominican Republic','Ecuador','Egypt','El Salvador','England','Eritrea','Estonia','Eswatini','Ethiopia',
                    'Fiji','Finland','France','Gabon','Gambia','Georgia','Germany','Ghana','Gibraltar','Greece','Greenland','Grenada','Guam','Guatemala','Guinea','Guyana','Haiti',
                    'Honduras','Hong Kong','Hungary','Iceland','India','Indonesia','Iran','Iraq','Ireland','Isle of Man','Israel','Italy','Jamaica','Japan','Jersey','Jordan','Kazakhstan',
                    'Kenya','Kiribati','Kosovo','Kuwait','Kyrgyzstan','Laos','Lativa','Lebanon',
                    'Lesotho','Liberia','Libya','Liechtenstein','Lithuania','Luxembourg','Macau','Madagascar','Malawi','Malaysia','Maldives','Mali','Malta','Mauritania','Mauritius',
                    'Mexico','Moldova','Monaco','Mongolia','Montenegro','Morocco','Mozambique','Myanmar','Namibia','Nauru','Nepal','Netherlands','New Zealand','Nicaragua','Niger','Nigeria',
                    'North Korea','North Macedonia','Norway','Oman','Pakistan','Palau','Palestine','Panam','Papua New Guinea','Paraguay','Peru','Philippines','Poland','Portugal','Puerto Rico','Qatar',
                    'Romania','Russia','Rwanda','Saint Lucia','Samoa','San Marino','Saudi Arabia','Scotland','Serbia','Senegal','Seychelles','Sierra Leone','Singapore',
                    'Slovakia','Slovenia','Solomon Islands','Somalia','South Africa','South Korea','South Sudan','Spain','Sri Lanka',
                    'Sudan','Suriname','Sweden','Switzerland','Syria','Taiwan','Tajikistan','Tanzania','Thailand','Togo','Tonga','Trinidad and Tobago','Tunisia','Turkey','Turkmenistan',
                    'Uganda','Ukraine','United Arab Emirates','United Kingdom','United States','Uruguay','Uzbekistan','Vanuatu','Vatican City','Venezuela','Vietnam',
                    'Wales','Yemen','Zambia','Zimbabwe'
                ]
    response = random.choice(countries)
    channel = bot.get_channel(933482401605247066)
    await channel.send(file=discord.File('C:\Users\emre-\Desktop\Coding\DcBot\flags' + response + '.png'))
    def check(message):
        return message.content == response and message.channel == channel
    try:
        message = await bot.wait_for("message", timeout=10.0, check=check)
        await ctx.send(f"Yes!"+ message.author.mention + " it was " + "**" + response + "**")
    except asyncio.TimeoutError:
        await channel.send(f"The right answer would've been " + "**" + response + "**")

@bot.command(name='roll', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice) +ctx.message.author.mention )

@bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

bot.run(TOKEN)
