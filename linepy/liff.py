# -*- coding: utf-8 -*-
from akad.ttypes import *
import json, requests

def loggedIn(func):
    def checkLogin(*args, **kwargs):
        if args[0].isLogin:
            return func(*args, **kwargs)
        else:
            args[0].callback.other('You want to call the function, you must login to LINE')
    return checkLogin

class Liff(object):
    isLogin = False

    def __init__(self):
        self.isLogin = True

    @loggedIn
    def issueLiffView(self, to):
        az = LiffChatContext(to)
        ax = LiffContext(chat=az)
        lf = LiffViewRequest('1653635854-BmgzeMGk', ax)
        return self.liff.issueLiffView(lf)
        
    @loggedIn
    def allowLiff(self):
        url = 'https://access.line.me/dialog/api/permissions'
        data = {
            'on': [
                'P',
                'CM'
            ],
            'off': []
        }
        headers = {
            'X-Line-Access': self.authToken,
            'X-Line-Application': self.server.APP_NAME,
            'X-Line-ChannelId': '1653635854',
            'Content-Type': 'application/json'
        }
        requests.post(url, json=data, headers=headers)

    @loggedIn
    def postTemplate(self, to, data):
        self.allowLiff()
        token = self.issueLiffView(to)
        url = 'https://api.line.me/message/v3/share'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer %s' % token.accessToken
        }
        data = {
            'messages': [data]
        }
        res = requests.post(url, headers=headers, data=json.dumps(data))
        return res
        
    @loggedIn
    def postFlex(self, to, data='', altText=''):
        self.allowLiff()
        token = self.issueLiffView(to)
        url = 'https://api.line.me/message/v3/share'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer %s' % token.accessToken
        }
        anu = {
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "Isi datanya asw !!!",
                                "wrap": True,
                                "color": "#000000",
                                "size" : "sm"
                            }
                        ]
                    }
                }
        altText = altText if altText else '%s sent a messages' % self.profile.displayName
        data = data if data else anu
        data = {
            'messages': [{'type': 'flex', 'altText' : altText, 'contents' : data}]
        }
        res = requests.post(url, headers=headers, data=json.dumps(data))
        return res

    @loggedIn
    def issueLiffSquareView(self, to):
        az = LiffSquareChatContext(to)
        ax = LiffContext(squareChat=az)
        lf = LiffViewRequest('1653635854-BmgzeMGk', ax)
        return self.liff.issueLiffView(lf)

    @loggedIn
    def postSquareTemplate(self, to, data):
        self.allowLiff()
        token = self.issueLiffSquareView(to)
        url = 'https://api.line.me/message/v3/share'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer %s' % token.accessToken
        }
        data = {
            'messages': [data]
        }
        res = requests.post(url, headers=headers, data=json.dumps(data))
        return res

