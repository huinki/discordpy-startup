from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
CHANNEL_ID = 793419776591396864 #チャンネルID

GLOBAL_LIST = []
GLOBAL_START_FLG = True

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@client.event
async def on_message(message):
    print(GLOBAL_LIST)
    print(GLOBAL_START_FLG)
    if GLOBAL_START_FLG == False:
    # 「おはよう」で始まるか調べる
        print("中きてる")
        if message.content.startswith("list"):
            if client.user != message.author:
                if len(GLOBAL_LIST) != 0:
                    # メッセージを書きます
                    m = "```" + "現在参加予定" + str(len(GLOBAL_LIST)) + "名 \n"
                    # メッセージが送られてきたチャンネルへメッセージを送ります
                    # メッセージを書きます
                    index = 0
                    for user in GLOBAL_LIST:
                        if index == 0:
                            m = m + user
                        else:
                            m = m + ", " + user 
                        if index != len(GLOBAL_LIST) - 1:
                            m = m + "\n"
                    # メッセージが送られてきたチャンネルへメッセージを送ります
                    m = m + "```"
                    await message.channel.send(m)
                else:
                    m = "現在参加者はいません"
                    await message.channel.send(m)
        if message.content.startswith("いける"):
            # 送り主がBotだった場合反応したくないので
            if client.user != message.author:
                if message.author.name in GLOBAL_LIST:
                    # メッセージを書きます
                    m = "てめえはもう答えただろ"
                else:
                    # メッセージを書きます
                    m = "```" + message.author.name + "参加予定～ \n"
                    # メッセージが送られてきたチャンネルへメッセージを送ります
                    GLOBAL_LIST.append(message.author.name)
                    # メッセージを書きます
                    m = m + "現在参加予定" + str(len(GLOBAL_LIST)) + "名 \n"
                    # メッセージが送られてきたチャンネルへメッセージを送ります
                    # メッセージを書きます
                    index = 0
                    for user in GLOBAL_LIST:
                        if index == 0:
                            m = m + user
                        else:
                            m = m + ", " + user 
                        if index != len(GLOBAL_LIST) - 1:
                            m = m + "\n"
                    # メッセージが送られてきたチャンネルへメッセージを送ります
                    m = m + "```"
                    await message.channel.send(m)
        # 「おはよう」で始まるか調べる
        if message.content.startswith("いけない"):
            # 送り主がBotだった場合反応したくないので
            if client.user != message.author:
                if message.author.name in GLOBAL_LIST:
                    # メッセージを書きます
                    m = "てめえはもう答えただろ"
                else:
                    # メッセージを書きます
                    m = "調整お願いします"
                    # メッセージが送られてきたチャンネルへメッセージを送ります
                    await message.channel.send(m)
        if message.content.startswith("いけなくなった"):
            # 送り主がBotだった場合反応したくないので
            if client.user != message.author:
                if message.author.name in GLOBAL_LIST:
                    # メッセージを書きます
                    m = "ぴえん"
                    await message.channel.send(m)
                    if len(GLOBAL_LIST) != 0:
                        GLOBAL_LIST.remove(message.author.name)
                        # メッセージを書きます
                        m = "```" + "現在参加予定" + str(len(GLOBAL_LIST)) + "名 \n"
                        # メッセージが送られてきたチャンネルへメッセージを送ります
                        # メッセージを書きます
                        index = 0
                        for user in GLOBAL_LIST:
                            if index == 0:
                                m = m + user
                            else:
                                m = m + ", " + user 
                            if index != len(GLOBAL_LIST) - 1:
                                m = m + "\n"
                        # メッセージが送られてきたチャンネルへメッセージを送ります
                        m = m + "```"
                        await message.channel.send(m)
                    else:
                        m = "現在参加者はいません"
                        await message.channel.send(m)
                else:
                    # メッセージを書きます
                    m = "元から参加予定じゃねえだろタコスケ"
                    # メッセージが送られてきたチャンネルへメッセージを送ります
                    await message.channel.send(m)

# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    # 現在の曜日
    week = datetime.now().strftime('%A')
    if week == 'Saturday':
        if now == '19:00':	
            global GLOBAL_START_FLG
            GLOBAL_START_FLG = False
            global GLOBAL_LIST
            GLOBAL_LIST = []
            channel = client.get_channel(CHANNEL_ID)
            print(GLOBAL_START_FLG)
            await channel.send('明日AmongUsいける方どうぞ↓　いける/いけない')  

#ループ処理実行
loop.start()


bot.run(token)
