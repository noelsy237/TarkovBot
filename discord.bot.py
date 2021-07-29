import os
from dotenv import load_dotenv
import random
import discord
from discord.ext import commands

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix='!')
client.remove_command('help')


@client.event
async def on_ready():
    activity = discord.Game(name="Escape from Tarkov", type=3)
    await client.change_presence(activity=activity)
    print('Success!')


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command, try `!help`.')
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send('You do not have permission to use this command.')


@client.command()
async def help(ctx):
    embed = discord.Embed(
        title='Command List',
        description='Try out any of the commands listed below.',
        colour=discord.Colour.blue()
    )
    embed.add_field(name='Random Kit', value='Use the command `!kit` to generate a random kit.', inline=False)
    embed.add_field(name='Random Ammo', value='To generate a random ammo type, use `!random_` followed by the calibre '
                                              'e.g. `!random_7.62x39mm`', inline=False)
    embed.add_field(name='Ammo Stats', value='To display a table of stats for a given calibre, use a `!` followed by '
                                             'the calibre e.g. `!7.62x39mm`', inline=False)
    embed.add_field(name='Clear', value='Use the command `!clear` to clear the previous command.', inline=False)

    await ctx.send(embed=embed)


@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=3):
    await ctx.channel.purge(limit=amount)


@client.command(aliases=['4.6x30', '4.6x30mm'])
async def _46x30__(ctx):
    embed = discord.Embed(
        title='HK 4.6x30mm',
        description='Find all stats for this calibre in the attached image',
        colour=discord.Colour.blue()
    )
    embed.set_image(url="https://i.ibb.co/Pr7Jffw/4-6x30.png")
    embed.set_footer(text='Statistics current as of 04/06/2021')
    await ctx.send(embed=embed)


@client.command(aliases=['5.7x28', '5.7x28mm', '5.7'])
async def _57x28__(ctx):
    embed = discord.Embed(
        title='5.7x28mm FN',
        description='Find all stats for this calibre in the attached image',
        colour=discord.Colour.blue()
    )
    embed.set_image(url="https://i.ibb.co/C9cm3xT/5-7x28.png")
    embed.set_footer(text='Statistics current as of 04/06/2021')
    await ctx.send(embed=embed)


@client.command(aliases=['5.45', '545', '5.45x39', '5.45x39mm'])
async def _545x39__(ctx):
    embed = discord.Embed(
        title='5.45x39mm',
        description='Find all stats for this calibre in the attached image',
        colour=discord.Colour.blue()
    )
    embed.set_image(url="https://i.ibb.co/whVHPZS/5-45x39.png")
    embed.set_footer(text='Statistics current as of 04/06/2021')
    await ctx.send(embed=embed)


@client.command(aliases=['5.56', '556', '5.56x45', '5.56x45mm'])
async def _556x45__(ctx):
    embed = discord.Embed(
        title='5.56x45mm NATO',
        description='Find all stats for this calibre in the attached image',
        colour=discord.Colour.blue()
    )
    embed.set_image(url="https://i.ibb.co/MC0Xx3V/5-56x45.png")
    embed.set_footer(text='Statistics current as of 04/06/2021')
    await ctx.send(embed=embed)


@client.command(aliases=['7.62x25', '7.62x25mm'])
async def _762x25__(ctx):
    embed = discord.Embed(
        title='7.62x25 Tokarev',
        description='Find all stats for this calibre in the attached image',
        colour=discord.Colour.blue()
    )
    embed.set_image(url="https://i.ibb.co/6b26XP8/7-62x25.png")
    embed.set_footer(text='Statistics current as of 04/06/2021')
    await ctx.send(embed=embed)


@client.command(aliases=['7.62x39', '7.62x39mm', '7.62', '762'])
async def _762x39__(ctx):
    embed = discord.Embed(
        title='7.62x39mm',
        description='Find all stats for this calibre in the attached image',
        colour=discord.Colour.blue()
    )
    embed.set_image(url="https://i.ibb.co/Rb9pxph/7-62x39.png")
    embed.set_footer(text='Statistics current as of 04/06/2021')
    await ctx.send(embed=embed)


@client.command(aliases=['7.62x51', '7.62x51mm'])
async def _762x51__(ctx):
    embed = discord.Embed(
        title='7.62x51mm NATO',
        description='Find all stats for this calibre in the attached image',
        colour=discord.Colour.blue()
    )
    embed.set_image(url="https://i.ibb.co/NY6GSp4/7-62x51.png")
    embed.set_footer(text='Statistics current as of 04/06/2021')
    await ctx.send(embed=embed)


@client.command(aliases=['7.62x54', '7.62x54mm', '7.62x54mmr', 'mosin'])
async def _762x54__(ctx):
    embed = discord.Embed(
        title='7.62x54mmR',
        description='Find all stats for this calibre in the attached image',
        colour=discord.Colour.blue()
    )
    embed.set_image(url="https://i.ibb.co/WHQg90j/7-62x54.png")
    embed.set_footer(text='Statistics current as of 04/06/2021')
    await ctx.send(embed=embed)


@client.command(aliases=['9x18', '9x18mm'])
async def _9x18__(ctx):
    embed = discord.Embed(
        title='9x18mm',
        description='Find all stats for this calibre in the attached image',
        colour=discord.Colour.blue()
    )
    embed.set_image(url="https://i.ibb.co/9NfFsM8/9x18.png")
    embed.set_footer(text='Statistics current as of 04/06/2021')
    await ctx.send(embed=embed)


@client.command(aliases=['9x19', '9x19mm', '9mm'])
async def _9x19__(ctx):
    embed = discord.Embed(
        title='9x19mm Parabellum',
        description='Find all stats for this calibre in the attached image',
        colour=discord.Colour.blue()
    )
    embed.set_image(url="https://i.ibb.co/8Y1p50K/9x19.png")
    embed.set_footer(text='Statistics current as of 04/06/2021')
    await ctx.send(embed=embed)


@client.command(aliases=['9x21', '9x21mm'])
async def _9x21__(ctx):
    embed = discord.Embed(
        title='9x21mm Gyurza',
        description='Find all stats for this calibre in the attached image',
        colour=discord.Colour.blue()
    )
    embed.set_image(url="https://i.ibb.co/tKqSmfH/9x21.png")
    embed.set_footer(text='Statistics current as of 04/06/2021')
    await ctx.send(embed=embed)


@client.command(aliases=['9x39', '9x39mm'])
async def _9x39__(ctx):
    embed = discord.Embed(
        title='9x39mm',
        description='Find all stats for this calibre in the attached image',
        colour=discord.Colour.blue()
    )
    embed.set_image(url="https://i.ibb.co/4Zpn40t/9x39.png")
    embed.set_footer(text='Statistics current as of 04/06/2021')
    await ctx.send(embed=embed)


@client.command(aliases=['12.7', '12.7x55', '12.7x55mm'])
async def _127x55__(ctx):
    embed = discord.Embed(
        title='12.7x55mm STs-130',
        description='Find all stats for this calibre in the attached image',
        colour=discord.Colour.blue()
    )
    embed.set_image(url="https://i.ibb.co/qCmndSd/12-7x55.png")
    embed.set_footer(text='Statistics current as of 04/06/2021')
    await ctx.send(embed=embed)


@client.command(aliases=['12g', '12 gauge', '12x70', '12x70mm'])
async def _12g__(ctx):
    embed = discord.Embed(
        title='12 Gauge',
        description='Find all stats for this calibre in the attached image',
        colour=discord.Colour.blue()
    )
    embed.set_image(url="https://i.ibb.co/4gkN5Zc/12g.png")
    embed.set_footer(text='Statistics current as of 04/06/2021')
    await ctx.send(embed=embed)


@client.command(aliases=['20g', '20 gauge', '20x70', '20x70mm'])
async def _20g__(ctx):
    embed = discord.Embed(
        title='20 Gauge',
        description='Find all stats for this calibre in the attached image',
        colour=discord.Colour.blue()
    )
    embed.set_image(url="https://i.ibb.co/NLQTqBq/20g.png")
    embed.set_footer(text='Statistics current as of 04/06/2021')
    await ctx.send(embed=embed)


@client.command(aliases=['23x75', '23x75mm'])
async def _23x75__(ctx):
    embed = discord.Embed(
        title='23x75mm',
        description='Find all stats for this calibre in the attached image',
        colour=discord.Colour.blue()
    )
    embed.set_image(url="https://i.ibb.co/V2VbcYc/23x75.png")
    embed.set_footer(text='Statistics current as of 04/06/2021')
    await ctx.send(embed=embed)


@client.command(aliases=['40x46', '40x46mm', 'gl', 'gl40', 'gl-40'])
async def _40x46__(ctx):
    embed = discord.Embed(
        title='40x46mm',
        description='Find all stats for this calibre in the attached image',
        colour=discord.Colour.blue()
    )
    embed.set_image(url="https://i.ibb.co/RjwR7L4/40x46.png")
    embed.set_footer(text='Statistics current as of 04/06/2021')
    await ctx.send(embed=embed)


@client.command(aliases=['.45 acp', '45', '45 acp'])
async def _45__(ctx):
    embed = discord.Embed(
        title='.45 ACP',
        description='Find all stats for this calibre in the attached image',
        colour=discord.Colour.blue()
    )
    embed.set_image(url="https://i.ibb.co/8MNH10s/45-acp.png")
    embed.set_footer(text='Statistics current as of 04/06/2021')
    await ctx.send(embed=embed)


@client.command(aliases=['.300 blackout', '.300', '300', '300 blackout'])
async def _300__(ctx):
    embed = discord.Embed(
        title='.300 Blackout',
        description='Find all stats for this calibre in the attached image',
        colour=discord.Colour.blue()
    )
    embed.set_image(url="https://i.ibb.co/SQVncpS/300-blackout.png")
    embed.set_footer(text='Statistics current as of 04/06/2021')
    await ctx.send(embed=embed)


@client.command(aliases=['338', '338 lapua', '.338', '.338 lapua', '.338 lapua magnum', '338 lapua magnum'])
async def _338__(ctx):
    embed = discord.Embed(
        title='.338 Lapua Magnum',
        description='Find all stats for this calibre in the attached image',
        colour=discord.Colour.blue()
    )
    embed.set_image(url="https://i.ibb.co/L06GYp6/338-lap.png")
    embed.set_footer(text='Statistics current as of 04/06/2021')
    await ctx.send(embed=embed)


@client.command(aliases=['.366 tkm', '.366', '366'])
async def _366__(ctx):
    embed = discord.Embed(
        title='.366 TKM',
        description='Find all stats for this calibre in the attached image',
        colour=discord.Colour.blue()
    )
    embed.set_image(url="https://i.ibb.co/D8s91R5/366-tkm.png")
    embed.set_footer(text='Statistics current as of 04/06/2021')
    await ctx.send(embed=embed)


@client.command()
async def kit(ctx):
    weapon = ["ADAR 2-15 .223 Carbine", "AK-101 5.56x45 assault rifle", "AK-102 AK-102 5.56x45 assault rifle",
              "AK-103 7.62x39 assault rifle", "AK-104 7.62x39 assault rifle", "AK-105 5.45x39 assault rifle",
              "AK-74 5.45x39 assault rifle", "AK-74M 5.45x39 assault rifle", "AK-74N 5.45x39 assault rifle",
              "AKM 7.62x39 assault rifle", "AKMN 7.62x39 assault rifle", "AKMS 7.62x39 assault rifle",
              "AKMSN 7.62x39 assault rifle", "AKS-74 5.45x39 assault rifle", "AKS-74N 5.45x39 assault rifle",
              "Kalashnikov AKS-74U 5.45x39", "Kalashnikov AKS-74UB 5.45x39", "Kalashnikov AKS-74UN 5.45x39",
              "ASh-12 12.7x55 assault rifle", "AS VAL", "DT MDR 5.56x45 Assault Rifle",
              "DT MDR 7.62x51 Assault Rifle", "HK 416A5 5.56x45 Assault Rifle", "Kel-Tec RFB 7.62x51",
              "Colt M4A1 5.56x45 Assault Rifle", "SIG MCX .300 AAC Blackout Assault Rifle", "DS Arms SA-58 7.62x51",
              "Vepr AKM/VPO-209 366TKM carbine", "Vepr KM / VPO-136 7.62x39 carbine",
              "Simonov Semi-Automatic Carbine SKS 7.62x39 Hunting Rifle Version",
              "Simonov Semi-Automatic Carbine SKS 7.62x39", "Vepr Hunter/VPO-101 7.62x51 carbine",
              "RPK-16 5.45x39 light machine gun", "HK MP5 9x19 submachinegun (Navy 3 Round Burst)",
              "HK MP5 Kurz 9x19 submachinegun", "HK MP7A1 4.6x30 submachinegun", "HK MP7A2 4.6x30 submachinegun",
              "B&T MP9 9x19 submachinegun", "B&T MP9-N 9x19 Submachinegun", "SIG MPX 9x19 Submachine gun",
              "FN P90 5.7x28 submachinegun", "Submachinegun 19-01 Vityaz-SN 9x19", "PP-9 Klin 9x18PMM SMG",
              "PP-91 Kedr 9x18PM SMG", "Submachinegun PPSH-41 7.62x25", "Saiga-9 9x19 Carbine",
              "STM-9 Gen.2 9x19 carbine", "HK UMP 45 submachinegun", "TDI KRISS Vector Gen.2 .45 ACP submachinegun",
              "TDI Kriss Vector Gen.2 9x19 submachinegun", "Mossberg 590A1 12ga shotgun",
              "Remington Model 870 12ga shotgun", "MP-133 12ga shotgun", "MP-153 12ga semi-automatic shotgun",
              "Saiga 12ga ver.10 12x76 assault rifle", "TOZ-106 bolt-action shotgun", "TOZ KS-23M 23x75mm shotgun",
              "Lone Star TX-15 DML Rifle", "Springfield Armory M1A 7.62x51", "Mk-18 .338 LM marksman rifle",
              "Remington R11 RSASS 7.62x51",
              "Knight's Armament Company SR-25 7.62x51", "SVDS 7.62x54 Sniper rifle",
              "Special Sniper Rifle VSS Vintorez", "DVL-10 Saboteur sniper rifle", "Remington Model 700 Sniper rifle",
              "Mosin bolt-action sniper rifle", "Mosin bolt-action infantry rifle", "SV-98 bolt-action sniper rifle",
              "Orsis T-5000 .308 sniper rifle", "Molot VPO-215 .366 TKM rifle", "FN GL40 Mk.2 grenade launcher",
              "Stechkin Automatic Pistol 9x18PM", "Silenced Stechkin Automatic Pistol 9x18PM",
              "FN Five-seveN MK2 5.7x28 pistol", "FN Five-seveN MK2 FDE Frame 5.7x28 pistol", "GLOCK 17 9x19 pistol",
              "GLOCK 18C 9x19 pistol", "Colt M1911A1 .45 ACP pistol", "Colt M45A1 .45 ACP pistol",
              "Beretta M9A3 9x19 pistol", "Yarygin MP-443 Grach 9x19 pistol", "P226R 9x19 pistol",
              "PB 9x18PM silenced pistol", "PL-15 9x19 pistol", "PM (t) 9x18PM pistol", "PM 9x18PM pistol",
              "9x21 Serdyukov automatic pistol SR1MP Gyurza", "TT pistol 7.62x25 TT", "TT pistol 7.62x25 TT (gold)"]

    mods = ["None", "1", "2", "3", "4", "5", "Unlimited"]

    headwear = ["Armasight NVG mask", "Wilcox Skull Lock head mount", "Tac-Kek Fast MT Helmet (non-ballistic replica)",
                "Soft tank crew helmet TSH-4M-L", "Kolpak-1S riot helmet", "SHPM Firefighter's helmet",
                "PSH-97 'Djeta' helmet", "UNTAR helmet", "6B47 Ratnik-BSh Helmet", "6B47 Ratnik-BSh Helmet (floral)",
                "LZSh light helmet", "SSh-68 helmet (1968 steel helmet)", "Kiver-M Helmet",
                "DEVTAC Ronin ballistic helmet",
                "SSSh-95 Sfera-S (Sphere-S)", "MSA ACH TC-2001 MICH Series Helmet",
                "MSA ACH TC-2002 MICH Series Helmet",
                "MSA Gallet TC 800 High Cut combat helmet", "Highcom Striker ACHHC IIIA helmet (black)",
                "Highcom Striker ACHHC IIIA helmet (olive)", "ZSh-1-2M helmet",
                "Highcom Striker ULACH IIIA helmet (black)",
                "Highcom Striker ULACH IIIA helmet (tan)", "Diamond Age Bastion Helmet",
                "Ops-Core Fast MT SUPER HIGH CUT Helmet (black)", "Ops-Core Fast MT SUPER HIGH CUT Helmet (tan)",
                "Crye Precision Airframe Tan", "Team Wendy EXFIL Ballistic Helmet (black)",
                "Team Wendy EXFIL Ballistic Helmet (coyote)", "Galvion Caiman Ballistic Helmet",
                "BNTI LSHZ-2DTM Helmet",
                "Maska 1Sch helmet (green)", "Maska 1Sch helmet (Killa)", "Altyn helmet", "Rys-T helmet",
                "Vulkan-5 (LShZ-5) heavy helmet", "Kinda cowboy hat", "Ushanka ear-flap cap", "Miltec panama hat",
                "'Door Kicker' Boonie hat", "Shattered Mask"]

    headmods = ["None", "1", "2", "3", "Unlimited"]

    headset = ["GSSh-01 active headset", "MSA Sordin Supreme PRO-X/L active headphones", "Opsmen Earmor M32 headset",
               "Peltor ComTac 2 headset", "Peltor Tactical Sport headset", "Walker's Razor Digital headset",
               "Walker's XCEL 500BT Digital headset"]

    tacrig = ["Scav Vest", "Security vest", "DIY IDEA chest rig", "Spiritus Systems Bank Robber Chest Rig",
              "SOE Micro Rig",
              "Wartech gear rig (TV-109, TV-106)", "CSA chest rig", "UMTBS 6sh112 Scout-Sniper", "Splav Tarzan M22 Rig",
              "Haley Strategic D3CRX Chest Harness", "Triton M43-A Chest Harness",
              "Blackhawk! Commando Chest Harness (black)", "Blackhawk! Commando Chest Harness (tan)",
              "Direct Action Thunderbolt compact chest rig", "Gear Craft GC-BSS-MK1 rig", "Umka М33-SET1 hunter's vest",
              "LBT-1961A Load Bearing Chest Vest", "BlackRock chest rig", "Wartech MK3 chest rig (TV-104)",
              "ANA Tactical Alpha chest rig", "Azimut SS Jhuk Chest Harness (black)",
              "Azimut SS Jhuk Chest Harness (camo)",
              "Velocity Systems Multi-Purpose Patrol Vest", "Belt-A + Belt-B gear rig"]

    armour = ["6B5-16 Zh -86 'Uley' armored rig", "6B3TM-01M armored rig", "6B5-15 Zh -86 'Uley' armored rig",
              "ANA Tactical M2 armored rig", "ANA Tactical M1 armored rig", "Crye Precision AVS platecarrier",
              "Ars Arma A18 Skanda plate carrier", "Wartech TV-110 plate carrier", "5.11 Tactec plate carrier",
              "Ars Arma CPC MOD.2 plate carrier", "Module-3M bodyarmor", "PACA Soft Armor",
              "PACA Soft Armor (Rivals edition)", "6B2 armor (flora)", "MF-UNTAR armor vest", "Zhuk-3 Press armor",
              "6B23-1 armor (digital flora pattern)", "BNTI Kirasa-N armor", "Highcom Trooper TFO armor (multicam)",
              "6B13 assault armor (green)", "6B23-2 armor (mountain flora pattern)", "BNTI Korund-VM armor",
              "FORT Redut-M body armor", "6B13 M assault armor (tan)", "IOTV Gen4 armor (high mobility kit)",
              "BNTI Gzhel-K armor", "FORT Defender-2 body armor", "IOTV Gen4 armor (assault kit)",
              "IOTV Gen4 armor (full protection)", "FORT Redut-T5 body armor", "5.11 Hexgrid plate carrier",
              "LBT 6094A Slick Plate Carrier", "Zhuk-6a heavy armor", "6B43 Zabralo-Sh 6A Armor"]

    backpack = ["6SH118 raid backpack", "LBT-2670 Slim Field Med Pack",
                "Mystery Ranch Blackjack 50 backpack (multicam)",
                "Eberlestock F4 Terminator load bearing backpack (tiger stripe)", "SSO 'Attack 2' raid backpack",
                "Pilgrim tourist backpack", "3V G Paratus 3-Day Operator's Tactical Backpack",
                "Eberlestock G2 Gunslinger II backpack (dry earth)", "Oakley Mechanism heavy duty backpack (black)",
                "Camelbak Tri-Zip Backpack", "Ana tactical Beta 2 battle backpack",
                "Eberlestock F5 Switchblade backpack (dry earth)", "Hazard4 Takedown sling backpack",
                "Wartech Berkut VV-102 backpack", "LBT-8005A Day Pack backpack", "Scav Backpack", "Flyye MBSS Backpack",
                "Sanitar bag", "Duffle bag", "LK 3F Transfer tourist backpack", "Transformer Bag", "VKBO army bag",
                "Tactical sling bag"]

    meds = ["None", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes"]

    grenades = ["None", "F-1 hand Grenade", "RGD-5 hand Grenade", "VOG-17 Khattabka Grenade",
                "VOG-25 Khattabka Grenade", "M67 hand Grenade", "RDG-2B Smoke Grenade", "Zarya stun Grenade"]

    stim = ["Combat stimulant injector SJ1 TGLabs", "Combat stimulant injector SJ9 TGLabs",
            "Combat stimulant injector SJ6 TGLabs", "Propital", "Hemostatic drug Zagustin", "Adrenaline injector",
            "Meldonin", "AHF1-M", "3-(b-TG)", "L1 (Norepinephrine)", "P22", "Cocktail 'Obdolbos'",
            "M.U.L.E. stimulator",
            "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None"]

    coms = ["No", "Yes", "Yes", "Yes", "Yes"]

    mapchoice = ["Customs", "Factory", "Interchange", "Woods", "The Lab", "Reserve", "Shoreline"]

    time = ["Night", "Day", "Day", "Day", "Day", "Day", "Day", "Day", "Day", "Day"]
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
    embed.add_field(name='───────────', value=f'**Tactical rig (if applicable):** '
                                              f'`{random.choice(tacrig)}`', inline=False)
    embed.add_field(name='───────────', value=f'**Backpack:** `{random.choice(backpack)}`', inline=False)
    embed.add_field(name='───────────', value=f'**Meds:** `{random.choice(meds)}`', inline=False)
    embed.add_field(name='───────────', value=f'**Stimulator:** `{random.choice(stim)}`', inline=False)
    embed.add_field(name='───────────', value=f'**Communication:** `{random.choice(coms)}`', inline=False)
    embed.add_field(name='───────────', value=f'**Map:** `{random.choice(mapchoice)}`', inline=False)
    embed.add_field(name='───────────', value=f'**Day/Night:** `{random.choice(time)}`', inline=False)

    await ctx.send(embed=embed)


@client.command(aliases=['random_23x752', 'random_23x75mm2'])
async def _23x752(ctx):
    _23x75_ = ["'Barricade'", "Shrapnel-10", "Shrapnel-25", "'Star'"]

    embed = discord.Embed(
        colour=discord.Colour.blue()
    )
    embed.add_field(name='\u200b', value=f'Random ammo: {random.choice(_23x75_)}', inline=False)

    await ctx.send(embed=embed)


@client.command(aliases=['random_23x75', 'random_23x75mm'])
async def _23x75(ctx):
    _23x75_ = ["'Barricade'", "Shrapnel-10", "Shrapnel-25", "'Star'"]
    await ctx.send(f'Random ammo type: 23x75mm {random.choice(_23x75_)}')


@client.command(aliases=['random_4.6x30', 'random_4.6x30mm'])
async def _46x30(ctx):
    _46x30_ = ["AP SX", "FMJ SX", "Subsonic SX", "Action SX"]
    await ctx.send(f'Random ammo type: 4.6x30mm {random.choice(_46x30_)}')


@client.command(aliases=['random_.366 tkm', 'random_.366', 'random_366'])
async def _366(ctx):
    _366_ = ["AP", "EKO", "FMJ", "Geska"]
    await ctx.send(f'Random ammo type: .366 TKM {random.choice(_366_)}')


@client.command(aliases=['random_.45acp', 'random_45', 'random_45acp'])
async def _45acp(ctx):
    _45acp_ = ["AP", "FMJ", "Lasermatch FMJ", "Hydra-Shock", "RIP"]
    await ctx.send(f'Random ammo type: .45 ACP {random.choice(_45acp_)}')


@client.command(aliases=['random_12g', 'random_12 gauge', 'random_12x70', 'random_12x70mm'])
async def _12g(ctx):
    _12g_ = ["AP-20", "Flechette", "Shell with .50 BMG", "FTX Custom Lite", "'Poleve-6u' Slug", "Dual Sabot Slug",
             "'Poleva-3' Slug", "Led Slug", "HP Slug Copper Sabot Premier", "Grizzly 40 Slug", "HP Slug 'SFormance'",
             "7mm Buckshot", "6.5mm 'Express'", "'Magnum'", "RIP", "5.25mm Buckshot"]
    await ctx.send(f'Random ammo type: 12x70mm {random.choice(_12g_)}')


@client.command(aliases=['random_20g', 'random_20gauge', 'random_20x70', 'random_20x70mm'])
async def _20g(ctx):
    _20g_ = ["'Poleva-6u' Slug", "Star Slug", "'Poleva-3' Slug", "Devastator Slug", "7.5mm Buckshot", "7.3mm Buckshot",
             "6.2mm Buckshot", "5.6mm Buckshot"]
    await ctx.send(f'Random ammo type: 20x70mm {random.choice(_20g_)}')


@client.command(aliases=['random_9x39', 'random_9x39mm'])
async def _9x39(ctx):
    _9x39_ = ["7N12 BP", "7N9 SPP", "SP-6", "SP-5"]
    await ctx.send(f'Random ammo type: 9x39mm {random.choice(_9x39_)}')


@client.command(aliases=['random_9x21', 'random_9x21mm'])
async def _9x21(ctx):
    _9x21_ = ["SP13", "SP10", "SP11", "SP12"]
    await ctx.send(f'Random ammo type: 9x21mm {random.choice(_9x21_)}')


@client.command(aliases=['random_9x19', 'random_9x19mm', 'random_9mm'])
async def _9x19(ctx):
    _9x19_ = ["7N31", "AP 6.3", "Pst gzh", "Green Tracer", "Luger CCI",
              "PSO gzh", "QuakeMaker", "RIP"]
    await ctx.send(f'Random ammo type: 9x19mm {random.choice(_9x19_)}')


@client.command(aliases=['random_9x18', 'random_9x18mm'])
async def _9x18(ctx):
    _9x18_ = ["PM PBM", "PM PMM", "PM 9 BZT gzh", "PM RG028 gzh", "PM  Pst gzh", "PM PPT gzh", "PM PPe gzh",
              "PM PRS gs",
              "PM PS gs PPO", "PM PSO gzh", "PM 9 P gzh", "PM PSV", "PM SP7 gzh", "PM SP8 gzh"]
    await ctx.send(f'Random ammo type: 9x18mm {random.choice(_9x18_)}')


@client.command(aliases=['random_5.7x28', 'random_5.7x28mm', 'random_5.7'])
async def _57x28(ctx):
    _57x28_ = ["SS190", "SB193", "L191", "SS197SR", "R37.X", "SS198LF", "R37.F"]
    await ctx.send(f'Random ammo type: 5.7x28mm {random.choice(_57x28_)}')


@client.command(aliases=['random_.300 blackout', 'random_.300', 'random_300', 'random_300blackout'])
async def _300(ctx):
    _300_ = ["AP", "BPZ"]
    await ctx.send(f'Random ammo type: .300 AAC Blackout {random.choice(_300_)}')


@client.command(aliases=['random_7.62x39', 'random_7.62x39mm', 'random_7.62', 'random_762'])
async def _762x39(ctx):
    _762x39_ = ["MAI AP", "BP", "PS", "T45M", "US", "HP"]
    await ctx.send(f'Random ammo type: 7.62x39mm {random.choice(_762x39_)}')


@client.command(aliases=['random_7.62x51', 'random_7.62x51mm'])
async def _762x51(ctx):
    _762x51_ = ["M993", "M61", "M62", "M80", "TPZ SP", "BPZ FMJ", "Ultra Nosler"]
    await ctx.send(f'Random ammo type: 7.62x51mm {random.choice(_762x51_)}')


@client.command(aliases=['random_7.62x54', 'random_7.62x54mm', 'random_7.62x54mmr', 'random_mosin'])
async def _762x54(ctx):
    _762x54_ = ["7N37", "SNB", "7BT1", "7N1 Sniper", "LPS Gzh", "T-46M"]
    await ctx.send(f'Random ammo type: 7.62x54mmR {random.choice(_762x54_)}')


@client.command(aliases=['random_338', 'random_338 lapua', 'random_.338', 'random_.338lapua',
                         'random .338 lapua magnum', 'random 338 lapua magnum'])
async def _338(ctx):
    _338_ = ["AP", "FMJ", "UPZ", "TAC-X"]
    await ctx.send(f'Random ammo type: .338 Lapua Magnum {random.choice(_338_)}')


@client.command(aliases=['random_7.62x25', 'random_7.62x25mm'])
async def _762x25(ctx):
    _762x25_ = ["Pst gzh", "PT gzh", "P gl", "AKBS", "FMJ43", "LRN", "LRNPC"]
    await ctx.send(f'Random ammo type: 7.62x25mm {random.choice(_762x25_)}')


@client.command(aliases=['random_5.56', 'random_556', 'random_5.56x45', 'random_5.56x45mm'])
async def _556x45(ctx):
    _556x45_ = ["SSA AP", "M995", "M855A1", "M856A1", "M855", "55 FMJ", "M856", "Mk 318 Mod 0 (SOST)", "MK 255 Mod 0",
                "55 HP", "Warmage"]
    await ctx.send(f'Random ammo type: 5.56x45mm {random.choice(_556x45_)}')


@client.command(aliases=['random_5.45', 'random_545', 'random_5.45x39', 'random_5.45x39mm'])
async def _545x39(ctx):
    _545x39_ = ["7N39 'Igolnik'", "BS", "BT", "BP", "PP", "PS", "T", "FMJ", "US", "PRS", "HP", "SP"]
    await ctx.send(f'Random ammo type: 5.56x45mm {random.choice(_545x39_)}')


@client.command(aliases=['random_12.7', 'random_12.7x55', 'random_12.7x55mm'])
async def _127x55(ctx):
    _127x55_ = ["PS12B", "PS12", "PS12A"]
    await ctx.send(f'Random ammo type: 12.7x55mm {random.choice(_127x55_)}')


client.run(token)
