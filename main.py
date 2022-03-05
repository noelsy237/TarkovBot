import os, random, discord, re, requests, datetime
from items import *
from dotenv import load_dotenv
from discord.ext import commands
from bs4 import BeautifulSoup
from textblob import TextBlob

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
client = commands.Bot(command_prefix='.')
client.remove_command('help')

@client.event
async def on_ready():
    activity = discord.Game(name="Escape from Tarkov", type=3)
    await client.change_presence(activity=activity)
    print('Success!')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command, try `.help`.')
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send('You do not have permission to use this command.')

@client.command()
async def help(ctx):
    embed = discord.Embed(
        title='Command List',
        description='Try out any of the commands listed below.',
        colour=discord.Colour.blue()
    )
    embed.add_field(name='Random Kit', value='Use the command `.kit` to generate a random kit.', inline=False)
    embed.add_field(name='Random Ammo', value='To generate a random ammo type, use `.rand` followed by the calibre '
                                              'e.g. `.rand 7.62x39mm`', inline=False)
    embed.add_field(name='Ammo Stats', value='To display a table of stats for a given calibre, use a `.stat` followed by '
                                             'the calibre e.g. `.stat 7.62x39mm`', inline=False)
    embed.add_field(name='Clear', value='Use the command `.clear` to clear the previous command.', inline=False)

    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=3):
    await ctx.channel.purge(limit=amount)

@client.command()
async def p(ctx, input=None):
    def searchAPI(string):
        itemQuery = '''\
            {
                itemsByName(name: "%s") {
                    name
                    shortName
                    types
                    lastLowPrice
                }\
            }
            ''' % (string)

        response = requests.post('https://tarkov-tools.com/graphql', json={'query': itemQuery})
        if response.status_code == 200:
            return response.json()['data']['itemsByName']
        else:
            raise Exception("Query failed to run by returning code of {}. {}".format(response.status_code, itemQuery))

    userInput = input
    itemsResult = searchAPI(userInput)

    if len(itemsResult) > 1:
        for item in itemsResult:
            resultEmbed = discord.Embed(
                title=f"{item['name']}",
                colour=discord.Colour.blue()
            )
            resultEmbed.add_field(name="Short Name:", value=f"{item['shortName']}", inline=False)
            resultEmbed.add_field(name="Type:", value=f"{item['types'][0]}", inline=False)
            resultEmbed.add_field(name="Last Price:", value=f"{item['lastLowPrice']}₽", inline=False)
            await ctx.send(embed=resultEmbed)
    else:
        await ctx.send("Item not found. Trying spell correct...")
        textBlb = TextBlob(userInput)
        textCorrected = textBlb.correct()
        itemsResult = searchAPI(textCorrected)
        if len(itemsResult) > 1:
            for item in itemsResult:
                resultEmbed = discord.Embed(
                    title=f"{item['name']}",
                    colour=discord.Colour.blue()
                )
                resultEmbed.add_field(name="Short Name:", value=f"{item['shortName']}", inline=False)
                resultEmbed.add_field(name="Type:", value=f"{item['types'][0]}", inline=False)
                resultEmbed.add_field(name="Last Price:", value=f"{item['lastLowPrice']}₽", inline=False)
                await ctx.send(embed=resultEmbed)

        else:
            await ctx.send("No items found, please try again.")
 
@client.command()
async def gpu(ctx, input=None):
    try:
        gpuAmount = int(input)

        if 0 < gpuAmount < 51:
            try:
                URL1 = "https://tarkov-market.com/item/graphics_card"
                GPU = requests.get(URL1)
                soup1 = BeautifulSoup(GPU.content, "html.parser")

                GPUClass = soup1.find("div", {"class": "big"})
                GPURawPrice = GPUClass.get_text()
                GPURawPrice2 = re.sub('[,₽]', '', GPURawPrice)
                GPURefinedPrice = int(GPURawPrice2)

                URL2 = "https://tarkov-market.com/item/physical_bitcoin_(btc)"
                BitCoin = requests.get(URL2)
                soup2 = BeautifulSoup(BitCoin.content, "html.parser")

                BitCoinClass = soup2.find("div", {"class": "big"})
                BitCoinRawPrice = BitCoinClass.get_text()
                BitCoinRawPrice2 = re.sub('[,₽]', '', BitCoinRawPrice)
                BitCoinRefinedPrice = int(BitCoinRawPrice2)

                ratePerHour = 1 / (145000 / (1 + (gpuAmount - 1) * 0.041225) / 3600)
                GPUCost = gpuAmount * GPURefinedPrice
                MoneyPerHour = BitCoinRefinedPrice * ratePerHour
                PayBackSeconds = (GPUCost / MoneyPerHour) * 3600
                PayBackTime = datetime.timedelta(seconds=PayBackSeconds)
                PayBackDays = PayBackTime.days
                PayBackHours = round(PayBackTime.seconds / 60 / 60)

                message = (f'With {gpuAmount} Graphics Cards, purchased at the current price of {GPURawPrice}, and the '
                           f'current price of bitcoin at {BitCoinRawPrice} it will take {PayBackDays} days and '
                           f'{PayBackHours} hours to pay for itself.')

                await ctx.send(message)

            except Exception as e:
                print(e)
        else:
            await ctx.send("Don't be silly.")
    except:
        await ctx.send("Don't be silly.")

@client.command()
async def stat(ctx, input=None):
    if input:
        for calibre in calibreTypes:
            if input in calibre['aliases']:
                embed = discord.Embed(
                    title=calibre['aliases'][0],
                    description='Find all stats for this calibre in the attached image',
                    colour=discord.Colour.blue(),
                )
                embed.set_image(url=calibre['image'])
                embed.set_footer(text='Statistics current as of 01/03/2022')
                await ctx.send(embed=embed)

    else:
        print("you need an input")

@client.command()
async def rand(ctx, input=None):
    if input:
        for calibre in calibreTypes:
            if input in calibre['aliases']:
                randomType = random.choice(calibre['types'])
                await ctx.send(f"Random ammo: `{randomType}`")

    else:
        await ctx.send('Input is required.')

@client.command()
async def kit(ctx):
    embed = discord.Embed(
        title='Random Kit',
        colour=discord.Colour.blue()
    )
    embed.add_field(name='───────────', value=f'**Weapon:** `{random.choice(weapon)}`', inline=False)
    embed.add_field(name='───────────', value=f'**Number of mods:** `{random.choice(mods)}`', inline=False)
    embed.add_field(name='───────────', value=f'**Grenades:** `{random.choice(grenades)}`', inline=False)
    embed.add_field(name='───────────', value=f'**Headwear:** `{random.choice(headwear)}`', inline=False)
    embed.add_field(name='───────────', value=f'**Headwear mods:** `{random.choice(headmods)}`', inline=False)
    embed.add_field(name='───────────', value=f'**Headset (if applicable):** `{random.choice(headset)}`', inline=False)
    embed.add_field(name='───────────', value=f'**Body armour:** `{random.choice(armour)}`', inline=False)
    embed.add_field(name='───────────', value=f'**Tactical rig (if applicable):** `{random.choice(tacrig)}`', inline=False)
    embed.add_field(name='───────────', value=f'**Backpack:** `{random.choice(backpack)}`', inline=False)
    embed.add_field(name='───────────', value=f'**Meds:** `{random.choice(meds)}`', inline=False)
    embed.add_field(name='───────────', value=f'**Injector:** `{random.choice(stim)}`', inline=False)
    embed.add_field(name='───────────', value=f'**Armband:** `{random.choice(armband)}`', inline=False)
    embed.add_field(name='───────────', value=f'**Communication:** `{random.choice(coms)}`', inline=False)
    embed.add_field(name='───────────', value=f'**Map:** `{random.choice(mapchoice)}`', inline=False)
    embed.add_field(name='───────────', value=f'**Day/Night:** `{random.choice(time)}`', inline=False)

    await ctx.send(embed=embed)

@client.command()
async def kits(ctx, user_input):
    day_night = random.choice(time)
    map_choice = random.choice(mapchoice)
    communication = random.choice(coms)

    user_input = int(user_input)
    
    if user_input >= 2 and user_input <= 5:
        while user_input > 0:
            user_input -= 1
            embed = discord.Embed(
                title=f'Random Kit (Player {user_input + 1})',
                colour=discord.Colour.blue()
            )
            embed.add_field(name='───────────', value=f'**Weapon:** `{random.choice(weapon)}`', inline=False)
            embed.add_field(name='───────────', value=f'**Number of mods:** `{random.choice(mods)}`', inline=False)
            embed.add_field(name='───────────', value=f'**Grenades:** `{random.choice(grenades)}`', inline=False)
            embed.add_field(name='───────────', value=f'**Headwear:** `{random.choice(headwear)}`', inline=False)
            embed.add_field(name='───────────', value=f'**Headwear mods:** `{random.choice(headmods)}`', inline=False)
            embed.add_field(name='───────────', value=f'**Headset (if applicable):** `{random.choice(headset)}`', inline=False)
            embed.add_field(name='───────────', value=f'**Body armour:** `{random.choice(armour)}`', inline=False)
            embed.add_field(name='───────────', value=f'**Tactical rig (if applicable):** `{random.choice(tacrig)}`', inline=False)
            embed.add_field(name='───────────', value=f'**Backpack:** `{random.choice(backpack)}`', inline=False)
            embed.add_field(name='───────────', value=f'**Meds:** `{random.choice(meds)}`', inline=False)
            embed.add_field(name='───────────', value=f'**Injector:** `{random.choice(stim)}`', inline=False)
            embed.add_field(name='───────────', value=f'**Armband:** `{random.choice(armband)}`', inline=False)
            embed.add_field(name='───────────', value=f'**Communication:** `{communication}`', inline=False)
            embed.add_field(name='───────────', value=f'**Map:** `{map_choice}`', inline=False)
            embed.add_field(name='───────────', value=f'**Day/Night:** `{day_night}`', inline=False)

            await ctx.send(embed=embed)
    else:
        await ctx.send("Input must be between 2 and 5.")

client.run(token)
