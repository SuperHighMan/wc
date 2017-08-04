#!/usr/bin/python3
#coding=utf8
from wxpy import *

bot = Bot()
myself = bot.self
bot.file_helper.send('Hello from baby!')

my_friend = ensure_one(bot.search('Baby'))
tuling = Tuling(api_key='e41c1168ef734f0e9585b7bd94e9c506')

# 使用图灵机器人自动与指定好友聊天
@bot.register(my_friend)
def reply_my_friend(msg):
    tuling.do_reply(msg)

embed()
