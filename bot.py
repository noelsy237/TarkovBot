import os, random, discord, re, requests, datetime, json, asyncio
from items import *
from dotenv import load_dotenv
from discord.ext import commands, tasks
from bs4 import BeautifulSoup
from textblob import TextBlob

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix='.', intents=intents)
client.remove_command('help')
intents.voice_states = True

# Setup bot details
@client.event
async def on_ready():
    activity = discord.Game(name="Escape from Tarkov", type=3)
    await client.change_presence(activity=activity)
    check_camera_status.start()
    check_deaf_status.start()
    print('Success!')

# Handler for insufficient permissions
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command, try `.help`')
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send('You do not have permission to use this command.')
    else:
        print(error)

# Return the help menu
@client.command()
async def help(ctx):
    embed = discord.Embed(
        title='Command List',
        description='Try out any of the commands listed below.',
        colour=discord.Colour.blue()
    )
    embed.add_field(name='Random Kit', value='Use the command `.kit` to generate a random kit. For a different kit for ' 
                         'multiple players, use the command `.kits`', inline=False)
    embed.add_field(name='Random Ammo', value='To generate a random ammo type, use `.rand` followed by the calibre '
                                              'e.g. `.rand 7.62x39mm`', inline=False)
    embed.add_field(name='Ammo Stats', value='To display a table of stats for a given calibre, use a `.stat` followed by '
                                             'the calibre e.g. `.stat 7.62x39mm`', inline=False)
    embed.add_field(name='GPU', value='Use the command `.gpu` followed by the number of GPUs you are looking to buy.', inline=False)
    embed.add_field(name='Clear', value='Use the command `.clear` to clear the previous command.', inline=False)

    await ctx.send(embed=embed)

@tasks.loop(seconds=30)    
async def check_camera_status():
    channel_id = 1204190077383745626
    channel = client.get_channel(channel_id)
    output_channel = client.get_channel(838386003227836439)

    if channel:
        for member in channel.members:
            if not member.voice.self_video:
                await member.move_to(None)
                await output_channel.send(f'{member.display_name} was kicked for not turning on their camera.')
                print(f'{member.display_name} was kicked for not turning on their camera.')

#original_channels = {}

#@tasks.loop(seconds=5)    
#async def check_deaf_status():
#    channel_ids = [1185031033364676648, 1191727879743094924, 1218755488150458418, 1007204325887582248, 814857337889488896, 1204190077383745626, 815140823024664586, 838030772577239090, 989690253315022868, 760793358280425492]
#    output_channel_id = 838386003227836439
#    loser_channel_id = 1219591417178099763
#    
#    output_channel = client.get_channel(output_channel_id)
#    loser_channel = client.get_channel(loser_channel_id)
#    
#    for channel_id in channel_ids:
#        channel = client.get_channel(channel_id)
#        if channel:
#            for member in channel.members:
#                if member.voice and member.voice.channel:
#                    if member.voice.self_deaf and 1228652251829112904 not in [role.id for role in member.roles]:
#                        original_channels[member.id] = member.voice.channel  # Store the original channel
#                        await member.move_to(loser_channel)
#                        await output_channel.send(f'{member.display_name} was kicked for being a loser.')

#@client.event
#async def on_voice_state_update(member, before, after):
#    if member.id in original_channels:
#        original_channel = original_channels[member.id]
#        if before.self_deaf and not after.self_deaf:
#            await member.move_to(original_channel)

# Return the price of an item (beta)
@client.command(aliases=['p'])
async def price(ctx, *, input=None):
    def searchPriceList(input):
        with open('data/items.json', 'r') as f:
            items = json.load(f)
        
        for item in items:
            if input in item['aliases'] or input == item['name']:
                return {'name': item['name'], 'short_name': item['aliases'][0], 'href': item['href']}

    def scrapePrice(href):
        endpoint = f"https://tarkov-market.com/item/{href}"
        request = requests.get(endpoint)
        scraper = BeautifulSoup(request.content, "html.parser")
        price = int(re.sub('[,₽]', '', ((scraper.find("div", {"class": "big"})).get_text())))
        return price

    def sendPriceEmbed(item):
        resultEmbed = discord.Embed(
                title=f"{item['name']}",
                colour=discord.Colour.blue()
            )
        resultEmbed.add_field(name="Short Name", value=item['short_name'], inline=False)
        resultEmbed.add_field(name="Last Price", value=f"{item['price']}₽", inline=False)
        resultEmbed.add_field(name="Market Link", value=f"https://tarkov-market.com/item/{item['href']}", inline=False)
        return(resultEmbed)

    if input:
        input.strip()
        item = searchPriceList(input)
        if item:
            item['price'] = scrapePrice(item['href'])
            await ctx.send(embed=sendPriceEmbed(item))
        # Try and auto correct each word in input
        else:
            await ctx.send("Item not found. Trying spell correct...")
            words = input.split(' ')
            correctedWords = ""
            for word in words:
                wordBlb = TextBlob(word)
                word = wordBlb.correct()
                correctedWords += str(word) + " "
                print(correctedWords)
                        
            href = searchPriceList(correctedWords.strip())
            if href:
                item['price'] = scrapePrice(item['href'])
                await ctx.send(embed=sendPriceEmbed(item))
            else:
                await ctx.send("No items found, please try again.")
    else:
        await ctx.send('Input required.')
 
# Solar calculation
@client.command()
async def solar(ctx):
    fuel = 166824
    euro = 13500000

    URL1 = "https://tarkov-market.com/item/Phased_array_element"
    AESA = requests.get(URL1)
    soup1 = BeautifulSoup(AESA.content, "html.parser")
    AESARefinedPrice = int(re.sub('[,₽]', '', ((soup1.find("div", {"class": "big"})).get_text())))
    URL2 = "https://tarkov-market.com/item/Working_LCD"
    LCD = requests.get(URL2)
    soup2 = BeautifulSoup(LCD.content, "html.parser")
    LCDRefinedPrice = int(re.sub('[,₽]', '', ((soup2.find("div", {"class": "big"})).get_text())))
    URL3 = "https://tarkov-market.com/item/Military_cable"
    mCable = requests.get(URL3)
    soup3 = BeautifulSoup(mCable.content, "html.parser")
    mCableRefinedPrice = int(re.sub('[,₽]', '', ((soup3.find("div", {"class": "big"}))).get_text()))
    URL4 = "https://tarkov-market.com/item/Military_power_filter"
    pFilter = requests.get(URL4)
    soup4 = BeautifulSoup(pFilter.content, "html.parser")
    pFilterRefinedPrice = int(re.sub('[,₽]', '', (soup4.find("div", {"class": "big"})).get_text()))

    # 75789 seconds per fuel. 1263.15 minutes, 21.0525 hours.
    total_cost = "{:,}".format(euro + (AESARefinedPrice * 4) + (LCDRefinedPrice * 3) + (mCableRefinedPrice * 10) + (pFilterRefinedPrice * 10))

    await ctx.send(f'Total cost: ₽{total_cost}')

# Return gpu calculations
@client.command()
async def gpu(ctx, input=None):
    try:
        gpuAmount = int(input)

        if 0 < gpuAmount < 51:
            try:
                URL1 = "https://tarkov-market.com/item/graphics_card"
                GPU = requests.get(URL1)
                soup1 = BeautifulSoup(GPU.content, "html.parser")
                GPURefinedPrice = int(re.sub('[,₽]', '', ((soup1.find("div", {"class": "big"})).get_text())))
                GPURawPrice = "{:,}".format(GPURefinedPrice)

                URL2 = "https://tarkov-market.com/item/physical_bitcoin_(btc)"
                BitCoin = requests.get(URL2)
                soup2 = BeautifulSoup(BitCoin.content, "html.parser")
                BitCoinRefinedPrice = int(re.sub('[,₽]', '', ((soup2.find("div", {"class": "big"})).get_text())))
                BitCoinRawPrice = "{:,}".format(BitCoinRefinedPrice)

                ratePerHour = 1 / (145000 / (1 + (gpuAmount - 1) * 0.041225) / 3600)
                GPUCost = gpuAmount * GPURefinedPrice
                MoneyPerHour = BitCoinRefinedPrice * ratePerHour
                PayBackSeconds = (GPUCost / MoneyPerHour) * 3600
                PayBackTime = datetime.timedelta(seconds=PayBackSeconds)
                PayBackDays = PayBackTime.days
                PayBackHours = round(PayBackTime.seconds / 60 / 60)

                message = (f'With {gpuAmount} Graphics Cards, purchased at the current price of `{GPURawPrice}`, and the '
                           f'current price of bitcoin at `{BitCoinRawPrice}` it will take {PayBackDays} days and '
                           f'{PayBackHours} hours to pay for itself.')

                await ctx.send(message)

            except Exception as e:
                print(e)
        else:
            await ctx.send("Must be in range of 1 and 50.")
    except:
        await ctx.send("Second input is required.")

# Return statistics for an item
@client.command()
async def stat(ctx, input=None):
    if input:
        for calibre in calibreTypes:
            if input in calibre['aliases']:
                embed = discord.Embed(
                    title=calibre['aliases'][0],
                    description='Find all stats for this calibre in the attached image',
                    colour=discord.Colour.blue()
                )
                embed.set_image(url=calibre['image'])
                embed.set_footer(text='Statistics current as of 01/03/2022')
                await ctx.send(embed=embed)
    else:
        await ctx.send('Input is required.')

# Return a random item
@client.command()
async def rand(ctx, input=None):
    if input:
        for calibre in calibreTypes:
            if input in calibre['aliases']:
                randomType = random.choice(calibre['types'])
                await ctx.send(f"Random ammo: `{randomType}`")
    else:
        await ctx.send('Input is required.')

# Generate a random kit
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
    embed.add_field(name='───────────', value=f'**Communication:** `{random.choice(coms)}`', inline=False)
    embed.add_field(name='───────────', value=f'**Map:** `{random.choice(mapchoice)}`', inline=False)
    embed.add_field(name='───────────', value=f'**Day/Night:** `{random.choice(time)}`', inline=False)

    await ctx.send(embed=embed)

# Generate a random kit for each member in a voice channel
@client.command()
async def kits(ctx):
    if ctx.author.voice and ctx.author.voice.channel:
        channel = client.get_channel(ctx.author.voice.channel.id)
        members = channel.members
        day_night = random.choice(time)
        map_choice = random.choice(mapchoice)
        communication = random.choice(coms)

        memberDetails = []
        for member in members:
            memberDetails.append({'id': member.id, 'name': member.name})
        
        for member in memberDetails:
            embed = discord.Embed(
                title=f'Random Kit',
                colour=discord.Colour.blue()
            )
            embed.add_field(name='Prepared for', value=f'<@!{member["id"]}>', inline=True)
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
            embed.add_field(name='───────────', value=f'**Communication:** `{communication}`', inline=False)
            embed.add_field(name='───────────', value=f'**Map:** `{map_choice}`', inline=False)
            embed.add_field(name='───────────', value=f'**Day/Night:** `{day_night}`', inline=False)

            await ctx.send(embed=embed)

    else:
        await ctx.send("You need to be in a voice channel for this command to work.")

# Run the bot
client.run(token)
