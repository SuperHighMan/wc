#!/usr/bin/python3
#coding=utf8

import itchat
import requests

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

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    defaultRepy = 'I received: ' + msg['Text']
    reply = get_response(msg['Text'])

    #return reply or defaultRepy
    print(reply)

@itchat.msg_register(itchat.content.PICTURE)
def attach_reply(msg):
    textReply = u'已下载'
    print(textReply)

itchat.auto_login(hotReload=True,enableCmdQR=False)
itchat.run()