import requests
import json

from khl import Bot, Message
from khl.card import CardMessage, Card, Module, Element, Types, Struct

# setup bot and tokens
with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

bot = Bot(token=config['token'])


# setup global variables
apiurl = "https://api.mcsrvstat.us/2/"


# on command 'status', make a request to apiurl adding the server ip 'repct.aimc.cc' to the end of the url
# extract online status, player count, player list and motd from the response
# send the extracted data to the channel
@bot.command('status')
async def status(msg: Message, bot: Bot):
    r = requests.get(apiurl + 'repct.aimc.cc')
    data = r.json()
    img_url = await bot.client.create_asset('top.png')
    try:
        online = data['online']
        print(online)
        players = data['players']['online']
        print(players)
        playerlist = data['players']['list']
        print(playerlist)
        motd = data['motd']['clean']
        print(motd)
        cm = CardMessage()
        c1 = Card(Module.Header('RE:PhiCraft Server Status'))
        c1.append(Module.Container(Element.Image(src=img_url)))
        c1.append(Module.Divider())
        c1.append(Module.Section(f"**Server is online**: {online}\n"
                                f"**Player count**: {players}\n"
                                f"**Player list**: {playerlist}\n"
                                f"**Server MOTD**: {motd}"))
        cm.append(c1)
        await msg.reply(cm)
    except:
        online = data['online']
        print(online)
        cm = CardMessage()
        c1 = Card(Module.Header('RE:PhiCraft Server Status'))
        c1.append(Module.Container(Element.Image(src=img_url)))
        c1.append(Module.Divider())
        c1.append(Module.Section(f"**Server is online**: {online}\n"
                                 f"**REPORT THIS TO THE SERVER ADMINISTRATOR ASAP**"))
        cm.append(c1)
        await msg.reply(cm)


bot.run()
