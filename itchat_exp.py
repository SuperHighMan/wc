#!/usr/bin/python3
#coding=utf8

import itchat
import requests, time, random
from itchat.content import *

KEY = 'e41c1168ef734f0e9585b7bd94e9c506'
def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : 'wechat',
    }
    try:
        r = requests.post(apiUrl,data=data).json()
        return r.get('text')
    except:
        return

def think_like(low, high) :
    time.sleep(random.randint(low, high))
    return
'''
@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    defaultRepy = 'I received: ' + msg['Text']
    reply = get_response(msg['Text'])

    #return reply or defaultRepy
    print(reply)

@itchat.msg_register(itchat.content.PICTURE)
def attach_reply(msg):
    msg['Text'](msg['FileName'])
    textReply = u'已下载'
    print(textReply)
'''


@itchat.msg_register([TEXT, PICTURE, VIDEO], isFriendChat=True)
def friend_reply(msg):
    if msg['Type'] == itchat.content.TEXT :
        defaultRepy = 'I received: ' + msg['Text']
        reply = get_response(msg['Text'])
        print(reply)
        # reply as a human, time for input
        think_like(low=3, high=10)
        return reply or defaultRepy

    elif msg['Type'] == itchat.content.PICTURE :
        print(u'图片')
    else:
        print('Else BB')

@itchat.msg_register([TEXT, PICTURE, VIDEO], isGroupChat=True)
def group_reply(msg):
    if msg['isAt']:
        defaultRepy = u'好的，收到'
        reply = get_response(msg['Text'])
        print(defaultRepy)
        think_like(low=8, high=20)
        return reply or defaultRepy
    else:
        print(u'群聊:'+msg['Text'])

@itchat.msg_register(FRIENDS)
def add_friend(msg):
    itchat.add_friend(**msg['Text'])
    itchat.send_msg(u'欢迎加入，嘿嘿！！', msg['RecommendInfo']['UserName'])

itchat.auto_login(hotReload=True,enableCmdQR=False)
itchat.run()