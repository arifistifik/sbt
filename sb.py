# -*- coding: utf-8 -*-
from thrift.transport import TTransport,TSocket,THttpClient,TTransport,TZlibTransport
from thrift.protocol import TCompactProtocol,TMultiplexedProtocol,TProtocol
from thrift.server import THttpServer,TServer,TProcessPoolServer
from linepy import *
from akad.ttypes import *
from multiprocessing import Pool, Process
from time import sleep
from humanfriendly import format_timespan, format_size, format_number, format_length
import pytz, datetime, pafy, time, timeit, random, sys, ast, re, os, json, subprocess, threading, string, codecs, requests, tweepy, ctypes, urllib, wikipedia
from datetime import timedelta, date
from datetime import datetime
from urllib.parse import quote
from bs4 import BeautifulSoup
import youtube_dl
from zalgo_text import zalgo
from threading import Thread,Event
import wikipedia as wiki
requests.packages.urllib3.disable_warnings()
from ttypes import LoginRequest
import json, requests, LineService
from thrift.transport import THttpClient

botStart = time.time()
cl = LINE("ENaoOR7jsGlIhxfxBUUb.0PzLwS72Fl1EGGJMnIN3IW.7k4OIV4TbYJWJy52Z2RVtPMaOp+J47jcosfbrQ+QDUE=")
#cl = LINE("YOUR TOKEN")
#cl = LINE("Email","Password")

cl.log("Auth Token : " + str(cl.authToken))
channelToken = cl.getChannelResult()
cl.log("Channel Token : " + str(channelToken))
readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")

clMID = cl.profile.mid
clProfile = cl.getProfile()
clSettings = cl.getSettings()
oepoll = OEPoll(cl)
call = cl
read = json.load(readOpen)
settings = json.load(settingsOpen)

connect1 = 'CHROME'
Headers1 = {
        'User-Agent': "Line/9.22.1",
        'X-Line-Application': "CROMEOS\t2.1.5ARIFISTIFIK\t11.2.5",
        "x-lal": "ja-US_US",
    }
connect2 = 'WIN'
Headers2 = {
        'User-Agent': "Line/9.22.1",
        'X-Line-Application': "DESKTOPWIN\t5.5.5ARIFISTIFIK\t11.2.5",
        "x-lal": "ja-US_US",
    }
connect3 = 'ios'
Headers3 = {
        'User-Agent': "Line/9.22.1",
        'X-Line-Application': "IOSIPAD\t8.14.2\tiPhone OS\t11.2.5",
        "x-lal": "ja-US_US",
    }

settings = {
    "autoAdd": False,
    "autoJoin": False,
    "autoLeave": False,
    "autoRead": False,
    "lang":"JP",
    "commentPost": "DPK BOT HADIR BUAT LIKE STATUS KAMU \n Add my owner ID http://line.me/ti/p/~@cob0606n",
    "detectMention": True,
    "autoResponMessage": "Ngapain tag gua woy",
    "responsticker": False,
    "changeGroupPicture":[],
    "notifikasi": False,
    "Sider":{},
    "checkSticker": False,
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ],
    "mimic": {
        "copy": False,
        "status": False,
        "target": {}
    }
}


read = {
    "readPoint": {},
    "readMember": {},
    "readTime": {},
    "ROM": {}
}

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

cctv = {
    "cyduk":{},
    "point":{},
    "MENTION":{},
    "sidermem":{}
}

myProfile["displayName"] = clProfile.displayName
myProfile["statusMessage"] = clProfile.statusMessage
myProfile["pictureStatus"] = clProfile.pictureStatus

def restartBot():
    print ("[ INFO ] BOT RESETTED")
    time.sleep(3)
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def logError(text):
    cl.log("[ ERROR ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
        
def sendMention(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMessage(to, Message, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes._from = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
def RmentionMembers(to, mid):
    try:
        arrData = ""
        textx = "{} mention members\n1.".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        cl.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "╔══[Total {} User]\n╠ ".format(str(len(mid)))
        arr = []
        no = 1
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "╠ "
            else:
                try:
                    textx += "╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    pass
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False

def Camera(to, text):
    pilih = ("#FF0000","#E000CD","#57FF00")
    warna = random.choice(pilih)
    data = {
            "type": "flex",
            "altText": "ARIFISTIFIK",
            "contents": {
             "type": "bubble",
             "styles": {
               "header": {
                 "backgroundColor": "#0000FF",
               },
               "body": {
                 "backgroundColor": "#000000",
                 "separator": True,
                 "separatorColor": "#ffffff"
               },
               "footer": {
                 "backgroundColor": "#000080",
                 "separator": True
               }
             },
             "header": {
               "type": "box",
               "layout": "horizontal",
               "contents": [
                 {
                   "type": "text",
                   "text": "  SIDER MEMBERS",
                   "weight": "bold",
                   "color": warna,
                   "size": "xxl"
                 }
               ]
             },
             "hero": {
               "type": "image",
               "url": "https://obs.line-scdn.net/{}".format(cl.getContact(op.param2).pictureStatus),
               "size": "full",
               "aspectRatio": "20:13",
               "aspectMode": "cover",
               "action": {
                 "type": "uri",
                 "uri": "https://line.me/ti/p/~arifistifik"
                 }
               },
                   "type": "bubble",
                   "body": {
                       "type": "box",
                       "layout": "horizontal",
                       "contents": [
                           {
                               "type": "text",
                               "text": "Nama: {}".format(cl.getContact(op.param2).displayName),
                               "wrap": True,
                               "color": warna,
                               "align": "center"
                           }
                       ]
                   },
                   "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [{
                        "type": "button",
                        "style": "primary",
                        "color": warna,
                        "height": "sm",
                        "action": {
                            "type": "uri",
                            "label": "ADD ID LINE",
                            "uri": "https://line.me/ti/p/"+cl.getUserTicket().id
                            }													
                        },
                    {
                        "type": "spacer",
                        "size": "sm",
                    }],
                    "flex": 0
                }
            }
        }
    cl.postTemplate(op.param1, data)

def sendTemplates(to, data):
    data = data
    url = "https://api.line.me/message/v3/share"
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi Note 5 Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Mobile Safari/537.36 Line/8.1.1'  
    headers['Content-Type'] = 'application/json'  
    headers['Authorization'] = 'Bearer eyJhbGciOiJIUzI1NiJ9.5uMcEEHahauPb5_MKAArvGzEP8dFOeVQeaMEUSjtlvMV9uuGpj827IGArKqVJhiGJy4vs8lkkseiNd-3lqST14THW-SlwGkIRZOrruV4genyXbiEEqZHfoztZbi5kTp9NFf2cxSxPt8YBUW1udeqKu2uRCApqJKzQFfYu3cveyk.GoRKUnfzfj7P2uAX9vYQf9WzVZi8MFcmJk8uFrLtTqU'
    sendPost = requests.post(url, data=json.dumps(data), headers=headers)
    print(sendPost)
    return sendPost
def sendTextTemplate(to, text):
    data = {
            "type": "flex",
            "altText": "SELFBOT",
            "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#FF0042"
    }
  },
  "type": "bubble",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "contents": [
              {
                "text": text,
                "size": "md",
                "margin": "none",
                "color": "#FFFFFF",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  }
}
}
    cl.postTemplate(to, data)

def sendTextTemplateMaster(to, text):
    data = {
            "type": "flex",
            "altText": "SELFBOT",
            "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": text,
            "size": "sm",
            "weight": "bold",
            "wrap": True,
            "color": "#40ff00"
          }
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#7D00C1"
    },
    "footer": {
      "backgroundColor": "#03f5f1"
    },
    "header": {
      "backgroundColor": "#03f5f1"
    }
    },  
     "hero": {
     "type": "image",
     "aspectRatio": "20:13",
     "aspectMode": "cover",
     "url": "https://i.pinimg.com/474x/f5/95/3e/f5953e75376e51e38d909779b027d7f5--hack-online-email-address.jpg",
     "size": "full",
     "margin": "xl"
  },
  "footer": {
      "type": "box",
      "layout": "vertical",
      "contents": [{
          "type": "box",
          "layout": "horizontal",
          "contents": [{
              "type": "button",
              "flex": 3,
              "style": "primary",
              "color": "#ff0a3b",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "DPK",
                  "uri": "http://line.me/ti/p/~@cob0606n"
              }
          }, {
              "flex": 3,
              "type": "button",
              "style": "primary",
              "color": "#310dff",
              "margin": "sm",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "CREATOR",
                  "uri": "http://line.me/ti/p/~@cob0606n"
              }
          }]
      }]
  }
}
}
    cl.postTemplate(to, data)

def sendStickerTemplate(to, text):
    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
    to = op.param1
    data = {
                          "type": "template",
                          "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                          "template": {
                             "type": "image_carousel",
                             "columns": [
                              {
                                  "imageUrl": text,
                                  "size": "full", 
                                  "action": {
                                      "type": "uri",
                                      "uri": "http://line.me/ti/p/~@cob0606n"
           }                                                
 }
]
                          }
                      }
    cl.postTemplate(to, data)

def clBot(op):
    try:
        if op.type == 0:
            print ("[ 0 ] END OF OPERATION")
            return
        if op.type == 5:
            print ("[ 5 ] NOTIFIED ADD CONTACT")
            if settings["autoAdd"] == True:
                cl.sendMessage(op.param1, "Halo {} terimakasih telah menambahkan saya sebagai teman :D".format(str(cl.getContact(op.param1).displayName)))
        if op.type == 13:
            print ("[ 13 ] NOTIFIED INVITE GROUP")
            group = cl.getGroup(op.param1)
            if settings["autoJoin"] == True:
                cl.acceptGroupInvitation(op.param1)
        if op.type == 24:
            print ("[ 24 ] NOTIFIED LEAVE ROOM")
            if settings["autoLeave"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 25:
            print ("[ 25 ] SEND MESSAGE")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
                if text.lower() == 'help':
                       if msg.toType == 2:
                           data = {
  "contents": [
    {
      "styles": {
        "body": {
          "backgroundColor": "#7D00C1"
        },
        "footer": {
          "backgroundColor": "#7D00C1"
        },
        "header": {
          "backgroundColor": "#7D00C1"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "contents": [
              {
                "contents": [
                  {
                    "type": "text",
                    "text": "SELFBOT ONLY",
                    "size": "xl",
                    "wrap": True,
                    "weight": "bold",
                    "color": "#00FF00",
                    "align": "center"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "image",
        "url": "https://i.pinimg.com/474x/f5/95/3e/f5953e75376e51e38d909779b027d7f5--hack-online-email-address.jpg", #hp
        "aspectRatio": "2:1",
        "aspectMode": "cover",
        "size": "full",
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": "MENU HELP",
                    "color": "#00FFFF",
                    "wrap": True,
                    "weight": "bold",
                    "type": "text",
                    "size": "lg",
                    "align": "center"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": "║│ RESTART\n║│RUNTIME\n║│ STATUS\n║│ ABOUT\n║│ DELL(RCHAT)\n║│ MIMICDEL (@)\n║│ MIMICLIST\n║│ LURKING ON|OFF|RESET\n║│ LURKING",
                    "size": "xs",
                    "margin": "none",
                    "color": "#FFFF00",
                    "wrap": True,
                    "weight": "regular",
                    "type": "text"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      }, #batas
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
        "text": "DPKBOT",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#FFFF00",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/~@cob0606n",
        },
        "align": "center"
      },
      {
        "type": "separator",
        "color": "#FF0000"
      },  
      {
        "type": "text",
        "text": "VERSION",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#FFFF00",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/~@cob0606n"
        },
        "align": "center"
      },
        ]
      }
    },
    {
      "styles": {
        "body": {
          "backgroundColor": "#7D00C1"
        },
        "footer": {
          "backgroundColor": "#7D00C1"
        },
        "header": {
          "backgroundColor": "#7D00C1"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "contents": [
              {
                "contents": [
                  {
                    "type": "text",
                    "text": "SELFBOT ONLY",
                    "size": "xl",
                    "wrap": True,
                    "weight": "bold",
                    "color": "#00FF00",
                    "align": "center"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "image",
        "url": "https://i.pinimg.com/474x/f5/95/3e/f5953e75376e51e38d909779b027d7f5--hack-online-email-address.jpg", #hp
        "aspectRatio": "2:1",
        "aspectMode": "cover",
        "size": "full",
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": "MENU SETTINGS",
                    "color": "#00FFFF",
                    "wrap": True,
                    "weight": "bold",
                    "type": "text",
                    "size": "lg",
                    "align": "center"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": "║│ ALLSTATUS「On/Off」\n║│ RESTART\n║│ NOTIF「On/Off」\n║│ SIDER「On/Off」\n║│ AUTOADD「On/Off」\n║│ AUTOJOIN「On/Off」\n║│ AUTOLEAVE「On/Off」\n║│ AUTOREAD「On/Off」\n║│ CHECKSTICKER「On/Off」\n║│ DETECTMENTION「On/Off」",
                    "size": "xs",
                    "margin": "none",
                    "color": "#FFFF00",
                    "wrap": True,
                    "weight": "regular",
                    "type": "text"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      }, #batas
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
        "text": "DPKBOT",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#FFFF00",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/~@cob0606n",
        },
        "align": "center"
      },
      {
        "type": "separator",
        "color": "#FF0000"
      },  
      {
        "type": "text",
        "text": "VERSION",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#FFFF00",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/~@cob0606n"
        },
        "align": "center"
      },
        ]
      }
    },
    {
      "styles": {
        "body": {
          "backgroundColor": "#7D00C1"
        },
        "footer": {
          "backgroundColor": "#7D00C1"
        },
        "header": {
          "backgroundColor": "#7D00C1"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "contents": [
              {
                "contents": [
                  {
                    "type": "text",
                    "text": "SELFBOT ONLY",
                    "size": "xl",
                    "wrap": True,
                    "weight": "bold",
                    "color": "#00FF00",
                    "align": "center"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "image",
        "url": "https://i.pinimg.com/474x/f5/95/3e/f5953e75376e51e38d909779b027d7f5--hack-online-email-address.jpg", #hp
        "aspectRatio": "2:1",
        "aspectMode": "cover",
        "size": "full",
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": "MENU GROUP",
                    "color": "#00FFFF",
                    "wrap": True,
                    "weight": "bold",
                    "type": "text",
                    "size": "lg",
                    "align": "center"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": "║│ GROUPCREATOR\n║│ GROUPID\n║│ GROUPNAME\n║│ GROUPPICTURE\n║│ GROUPTICKET「On/Off」\n║│ GROUPTICKET\n║│ GROUPLIST\n║│ GROUPMEMBERLIST\n║│ GROUPINFO\n║│ TAG",
                    "size": "xs",
                    "margin": "none",
                    "color": "#FFFF00",
                    "wrap": True,
                    "weight": "regular",
                    "type": "text"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      }, #batas
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
        "text": "DPKBOT",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#FFFF00",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/~@cob0606n",
        },
        "align": "center"
      },
      {
        "type": "separator",
        "color": "#FF0000"
      },  
      {
        "type": "text",
        "text": "VERSION",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#FFFF00",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/~@cob0606n"
        },
        "align": "center"
      },
        ]
      }
    },
    {
      "styles": {
        "body": {
          "backgroundColor": "#7D00C1"
        },
        "footer": {
          "backgroundColor": "#7D00C1"
        },
        "header": {
          "backgroundColor": "#7D00C1"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "contents": [
              {
                "contents": [
                  {
                    "type": "text",
                    "text": "SELFBOT ONLY",
                    "size": "xl",
                    "wrap": True,
                    "weight": "bold",
                    "color": "#00FF00",
                    "align": "center"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "image",
        "url": "https://i.pinimg.com/474x/f5/95/3e/f5953e75376e51e38d909779b027d7f5--hack-online-email-address.jpg", #hp
        "aspectRatio": "2:1",
        "aspectMode": "cover",
        "size": "full",
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": "MENU SPECIAL",
                    "color": "#00FFFF",
                    "wrap": True,
                    "weight": "bold",
                    "type": "text",
                    "size": "lg",
                    "align": "center"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": "║│ MP4 JUDUL\n║│ MTOH「TGL-BLN-THN」 \n║│ KALENDER\n║│ YOUTUBE JUDUL\n║│ ASMAULHUSNA NO 1-99\n║│ SMULE IDSMULE\n║│ YTSEARCH JUDUL\n║│ MP3 JUDUL\n║│ AL-QURAN NOMOR 1-114\n║│ AYAT SAJADAH",
                    "size": "xs",
                    "margin": "none",
                    "color": "#FFFF00",
                    "wrap": True,
                    "weight": "regular",
                    "type": "text"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      }, #batas
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
        "text": "DPKBOT",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#FFFF00",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/~@cob0606n",
        },
        "align": "center"
      },
      {
        "type": "separator",
        "color": "#FF0000"
      },  
      {
        "type": "text",
        "text": "VERSION",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#FFFF00",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/~@cob0606n"
        },
        "align": "center"
      },
        ]
      }
    },
    {
      "styles": {
        "body": {
          "backgroundColor": "#7D00C1"
        },
        "footer": {
          "backgroundColor": "#7D00C1"
        },
        "header": {
          "backgroundColor": "#7D00C1"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "contents": [
              {
                "contents": [
                  {
                    "type": "text",
                    "text": "SELFBOT ONLY",
                    "size": "xl",
                    "wrap": True,
                    "weight": "bold",
                    "color": "#00FF00",
                    "align": "center"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "image",
        "url": "https://i.pinimg.com/474x/f5/95/3e/f5953e75376e51e38d909779b027d7f5--hack-online-email-address.jpg", #hp
        "aspectRatio": "2:1",
        "aspectMode": "cover",
        "size": "full",
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": "MENU SELF",
                    "color": "#00FFFF",
                    "wrap": True,
                    "weight": "bold",
                    "type": "text",
                    "size": "lg",
                    "align": "center"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": "║│ ME\n║│ MYMID \n║│ MYNAME\n║│ MYBIO\n║│ MYPICTURE\n║│ MYVIDEOPROFILE\n║│ MYCOVER\n║│ STEALMID @\n║│ STEALCONTACT @\n║│ STEALPICTURE @",
                    "size": "xs",
                    "margin": "none",
                    "color": "#FFFF00",
                    "wrap": True,
                    "weight": "regular",
                    "type": "text"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      }, #batas
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
        "text": "DPKBOT",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#FFFF00",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/~@cob0606n",
        },
        "align": "center"
      },
      {
        "type": "separator",
        "color": "#FF0000"
      },  
      {
        "type": "text",
        "text": "VERSION",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#FFFF00",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/~@cob0606n"
        },
        "align": "center"
      },
        ]
      }
    },
    {
      "styles": {
        "body": {
          "backgroundColor": "#7D00C1"
        },
        "footer": {
          "backgroundColor": "#7D00C1"
        },
        "header": {
          "backgroundColor": "#7D00C1"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "contents": [
              {
                "contents": [
                  {
                    "type": "text",
                    "text": "SELFBOT ONLY",
                    "size": "xl",
                    "wrap": True,
                    "weight": "bold",
                    "color": "#00FF00",
                    "align": "center"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "image",
        "url": "https://i.pinimg.com/474x/f5/95/3e/f5953e75376e51e38d909779b027d7f5--hack-online-email-address.jpg", #hp
        "aspectRatio": "2:1",
        "aspectMode": "cover",
        "size": "full",
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": "MENU LAINYA",
                    "color": "#00FFFF",
                    "wrap": True,
                    "weight": "bold",
                    "type": "text",
                    "size": "lg",
                    "align": "center"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": "║│ GETTOKEN\n║│ CHROME 1 \n║│ WIN 1\n║│ IOS 1\n║│ MIMIC ON|OFF\n║│ MIMIC @\n║│ MIMICDEL @\n║│ STEALNAME @\n║│ STEALBIO @\n║│ STEALCOVER @ ",
                    "size": "xs",
                    "margin": "none",
                    "color": "#FFFF00",
                    "wrap": True,
                    "weight": "regular",
                    "type": "text"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      }, #batas
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
        "text": "DPKBOT",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#FFFF00",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/~@cob0606n",
        },
        "align": "center"
      },
      {
        "type": "separator",
        "color": "#FF0000"
      },  
      {
        "type": "text",
        "text": "VERSION",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#FFFF00",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/~@cob0606n"
        },
        "align": "center"
      },
        ]   
      }
    }
  ],
  "type": "carousel"
}
                           cl.postFlex(to, data)

                elif msg.text.lower().startswith("scall "):
                                if msg.toType == 2:
                                    sep = text.split(" ")
                                    strnum = text.replace(sep[0] + " ","")
                                    num = int(strnum)
                                    cl.sendMessage(to, "Succesfully Spam Call to Group")
                                    for var in range(0,num):
                                       group = cl.getGroup(to)
                                       members = [mem.mid for mem in group.members]
                                       cl.acquireGroupCallRoute(to)
                                       cl.inviteIntoGroupCall(to, contactIds=members)

                elif msg.text.lower().startswith("smule "):
                            proses = text.split(" ")
                            urutan = text.replace(proses[0] + " ","")
                            count = urutan.split("-")
                            search = str(count[0])
                            r = requests.get("https://www.smule.com/"+search+"/performances/json")
                            data = json.loads(r.text)
                            if len(count) == 1:
                                no = 0
                                ret_ = "DAFTAR OC\n"
                                for aa in data["list"]:
                                    no += 1
                                    ret_ += "\n" + str(no) + ". " + str(aa["title"])
                                ret_ += "\n\nSelanjutnya ketik: smule {}-nomor\nuntuk melihat detailnya. ".format(str(search))
                                sendTextTemplate(msg.to,ret_)
                            elif len(count) == 2:
                                try:
                                    num = int(count[1])
                                    b = data["list"][num - 1]
                                    smule = str(b["web_url"])
                                    c = "Judul Oc: "+str(b["title"])
                                    c += "\nPembuat: "+str(b["owner"]["handle"])
                                    c += "\nTotal like: "+str(b["stats"]["total_loves"])+" like"
                                    c += "\nTotal comment: "+str(b["stats"]["total_comments"])+" comment"
                                    c += "\nStatus VIP: "+str(b["owner"]["is_vip"])
                                    c += "\nStatus Oc: "+str(b["message"])
                                    c += "\nCreated Oc: {}".format(b["created_at"][:10])
                                    c += "\nDidengarkan: {}".format(b["stats"]["total_listens"])+" orang"
                                    hasil = "Detail Record\n\n"+str(c)
                                    dl = str(b["cover_url"])
                                    cl.sendImageWithURL(msg.to,dl)
                                    cl.sendMessage(msg.to, hasil, {'AGENT_NAME': ' URL Smule','AGENT_LINK': 'https://www.smule.com/{}'.format(str(b['owner']['handle'])),'AGENT_ICON': 'https://png.icons8.com/color/50/000000/speaker.png' })
                                    with requests.session() as s:
                                        s.headers['user-agent'] = 'Mozilla/5.0'
                                        r = s.get("https://sing.salon/smule-downloader/?url=https://www.smule.com{}".format(urllib.parse.quote(smule)))
                                        data = BeautifulSoup(r.content, 'html5lib')
                                        get = data.select("a[href*=https://www.smule.com/redir?]")[0]
                                        title = data.findAll('h2')[0].text
                                        imag = data.select("img[src*=https://www.smule.com/redir?]")[0]
                                        if 'Smule.m4a' in get['download']:
                                            sendTextTemplate(msg.to,"Type: Audio\n\nPlease wait for audio...")
                                            cl.sendAudioWithURL(msg.to, get['href'])
                                        else:
                                            sendTextTemplate(msg.to,"Type: Video\n\nPlease wait for video...")
                                            cl.sendVideoWithURL(msg.to, get['href'])
                                except Exception as e:
                                    cl.sendMessage(msg.to,"DONE")
                elif "hbd" in msg.text.lower():
                        	if settings["responsticker"] == True:
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://3.bp.blogspot.com/-Tjdw2KiP9Bg/Wfnb6krqnbI/AAAAAAAMKF4/LOZXghvCTkcaTmfSe0Fwe8CnTdOdCPj-ACLcBGAs/s1600/AW601285_21.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~@cob0606n"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)
                elif text.lower() == 'dell':
                    cl.removeAllMessages(op.param2)
                    sendTextTemplate(to, "Menghapus Chat")
                elif text.lower() == 'speed':
                    start = time.time()
                    cl.sendMessage(to, "⭐")
                    cl.sendMessage(to, "⭐⭐")
                    cl.sendMessage(to, "⭐⭐⭐")
                    elapsed_time = time.time() - start
                    sendTextTemplate(to,format(str(elapsed_time)))
                elif text.lower() == 'restart':
                    sendTextTemplate(to, "Akan di restart...")
                    restartBot()
                elif text.lower() == 'runtime':
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    cl.sendMessage(to, "Bot Aktif Selama {}".format(str(runtime)))
                elif text.lower() == 'about':
                    try:
                        arr = []
                        owner = "ud296655acef67cbd5e8208e63629f78b"
                        creator = cl.getContact(owner)
                        contact = cl.getContact(clMID)
                        grouplist = cl.getGroupIdsJoined()
                        contactlist = cl.getAllContactIds()
                        blockedlist = cl.getBlockedContactIds()
                        timeNow = time.time()
                        runtime = timeNow - botStart
                        runtime = format_timespan(runtime)
                        ret_ = "╔ Country : INDONESIA "
                        ret_ += "\n╠ My Name : {}".format(contact.displayName)
                        ret_ += "\n╠ Group : {}".format(str(len(grouplist)))
                        ret_ += "\n╠ Friend : {}".format(str(len(contactlist)))
                        ret_ += "\n╠ Blocked : {}".format(str(len(blockedlist)))
                        ret_ += "\n╠ Runtime : {}".format(str(runtime))
                        ret_ += "\n╠ Version : Free v 1.1 by Dpk_bot"
                        ret_ += "\n╠ Creator : {}".format(creator.displayName)
                        ret_ += "\n╚ Git : https://github.com/arifistifik/sbt"
                        sendTextTemplateMaster(to, str(ret_))
                    except Exception as e:
                        cl.sendMessage(msg.to, str(e))
                elif text.lower() == 'status':
                    try:
                        ret_ = "━━━━┅═❉ই۝ई❉═┅━━━━\n          ❇    STATUS    ❇\n╭━━━━━━━━━━━━━━━━\n║╭❉ 🔵[ON]|[OFF]🔴 ❇\n║┝───────────────"
                        if settings["autoAdd"] == True: ret_ += "\n║│🔵 Auto Add [ON]"
                        else: ret_ += "\n║│🔴 Auto Add [OFF]"
                        if settings["autoJoin"] == True: ret_ += "\n║│🔵 Auto Join [ON]"
                        else: ret_ += "\n║│🔴 Auto Join [OFF]"
                        if settings["autoLeave"] == True: ret_ += "\n║│🔵 Auto Leave [ON]"
                        else: ret_ += "\n║│🔴 Auto Leave [OFF]"
                        if settings["autoRead"] == True: ret_ += "\n║│🔵 Auto Read [ON]"
                        else: ret_ += "\n║│🔴 Auto Read [OFF]"
                        if settings["notifikasi"] == True: ret_ += "\n║│🔵 Notif [ON]"
                        else: ret_ += "\n║│🔴 Notif [OFF]"
                        if settings["detectMention"] == True: ret_ += "\n║│🔵 Detect Mention [ON]"
                        else: ret_ += "\n║│🔴 Detect Mention [OFF]"
                        ret_ += "\n║┝───────────────\n║╰❉      DPK BOT      ❇\n╰━━━━━━━━━━━━━━━━\n━━━━┅═❉ই۝ई❉═┅━━━━"
                        sendTextTemplateMaster(to, str(ret_))
                    except Exception as e:
                        cl.sendMessage(msg.to, str(e))
                elif text.lower() == 'autoadd on':
                    settings["autoAdd"] = True
                    sendTextTemplate(to, "mengaktifkan Auto Add")
                elif text.lower() == 'autoadd off':
                    settings["autoAdd"] = False
                    sendTextTemplate(to, "menonaktifkan Auto Add")
                elif text.lower() == 'autojoin on':
                    settings["autoJoin"] = True
                    sendTextTemplate(to, "mengaktifkan Auto Join")
                elif text.lower() == 'autojoin off':
                    settings["autoJoin"] = False
                    sendTextTemplate(to, "menonaktifkan Auto Join")
                elif text.lower() == 'autoleave on':
                    settings["autoLeave"] = True
                    sendTextTemplate(to, "mengaktifkan Auto Leave")
                elif text.lower() == 'autojoin off':
                    settings["autoLeave"] = False
                    sendTextTemplate(to, "menonaktifkan Auto Leave")
                elif text.lower() == 'autoread on':
                    settings["autoRead"] = True
                    sendTextTemplate(to, "mengaktifkan Auto Read")
                elif text.lower() == 'autoread off':
                    settings["autoRead"] = False
                    sendTextTemplate(to, "menonaktifkan Auto Read")
                elif text.lower() == 'checksticker on':
                    settings["checkSticker"] = True
                    sendTextTemplate(to, "mengaktifkan Check Details Sticker")
                elif text.lower() == 'checksticker off':
                    settings["checkSticker"] = False
                    sendTextTemplate(to, "menonaktifkan Check Details Sticker")
                elif text.lower() == 'responsticker on':
                    settings["responsticker"] = True
                    sendTextTemplate(to, "mengaktifkan Template Sticker")
                elif text.lower() == 'responsticker off':
                    settings["responsticker"] = False
                    sendTextTemplate(to, "menonaktifkan Template Sticker")
                elif text.lower() == 'detectmention on':
                    settings["datectMention"] = True
                    sendTextTemplate(to, "mengaktifkan Detect Mention")
                elif text.lower() == 'detectmention off':
                    settings["datectMention"] = False
                    sendTextTemplate(to, "menonaktifkan Detect Mention")

                elif text.lower() == 'allstatus on':
                    settings["notifikasi"] = True
                    settings["autoAdd"] = True
                    settings["autoJoin"] = True
                    settings["autoLeave"] = True
                    settings["autoRead"] = True
                    settings["datectMention"] = True
                    sendTextTemplate(to, "Allstatus bot mode on")

                elif text.lower() == 'allstatus off':
                    settings["notifikasi"] = False
                    settings["autoAdd"] = False
                    settings["autoJoin"] = False
                    settings["autoLeave"] = False
                    settings["autoRead"] = False
                    settings["datectMention"] = False
                    sendTextTemplate(to, "Allstatus bot mode on")

                elif text.lower() == 'mycontact':
                    sendMessageWithMention(to, clMID)
                    cl.sendContact(to, clMID)
                elif text.lower() == 'mymid':
                    cl.sendMessage(msg.to,"[MID]\n" +  clMID)
                elif text.lower() == 'myname':
                    me = cl.getContact(clMID)
                    cl.sendMessage(msg.to,"[DisplayName]\n" + me.displayName)
                elif text.lower() == 'mybio':
                    me = cl.getContact(clMID)
                    sendTextTemplate(msg.to,"[StatusMessage]\n" + me.statusMessage)
                elif text.lower() == 'mypicture':
                    me = cl.getContact(clMID)
                    cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                elif text.lower() == 'myvideoprofile':
                    me = cl.getContact(clMID)
                    cl.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                elif text.lower() == 'mycover':
                    me = cl.getContact(clMID)
                    cover = cl.getProfileCoverURL(clMID)    
                    cl.sendImageWithURL(msg.to, cover)
                elif msg.text.lower().startswith("stealcontact "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = cl.getContact(ls)
                            mi_d = contact.mid
                            cl.sendContact(msg.to, mi_d)
                elif msg.text.lower().startswith("mtoh "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = requests.get("http://api.aladhan.com/v1/gToH?date={}".format(txt))
                                data = url.json()
                                result = "~ Hijriah ~ = {}".format(str(data["data"]["hijri"]["date"]))
                                result += "\n~ Masehi ~ = {}".format(str(data["data"]["gregorian"]["date"]))
                                sendTextTemplate(to, result)

                elif msg.text.lower().startswith("asmaulhusna "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = requests.get("http://api.aladhan.com/asmaAlHusna/{}".format(txt))
                                data = url.json()
                                result = "~ Asma Allah ke {} = ~ {} ~".format(txt,data["data"][0]["name"])
                                result += "\n~Artinya =~ {} ~".format(data["data"][0]["en"]["meaning"])
                                sendTextTemplate(to, result)

                elif msg.text.lower().startswith("al-quran "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                web = requests.get("http://api.alquran.cloud/surah/{}".format(txt))
                                data = web.json()
                                result = "~[~{}~]~".format(data["data"]["englishName"])
                                quran = data["data"]
                                result += "\n~ Surah ke {} ~".format(quran["number"])
                                result += "\n~ Nama Surah ~ {} ~".format(quran["name"])
                                result += "\n~ {} Ayat ~".format(quran["numberOfAyahs"])
                                result += "\n~ {} ~".format(quran["name"])
                                result += "\n~ Ayat Sajadah = {} ~".format(quran["ayahs"][0]["sajda"])
                                result += "\n==================\n"
                                no = 0
                                for ayat in data["data"]["ayahs"]:
                                    no += 1
                                    result += "\n{}. {}".format(no,ayat['text'])
                                k = len(result)//10000
                                for aa in range(k+1):
                                    sendTextTemplate(to,'{}'.format(result[aa*10000 : (aa+1)*10000]))

                elif msg.text.lower().startswith("ayat sajadah"):
                                url = requests.get("http://api.alquran.cloud/sajda/quran-uthmani")
                                data = url.json()
                                result = "~[Ayat Sajadah]~"
                                for ayat in data["data"]["ayahs"]:
                                    ayatnya = ayat["text"]
                                    result += "\n{}".format(ayatnya)
                                    result += "\n Surah {}".format(ayat["surah"]["englishName"])
                                result += "\n ~~~~~~ Juz {} ~~~~~~".format(ayat["juz"])
                                sendTextTemplate(to, result)
                elif msg.text.lower().startswith("stealmid "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = "[ Mid User ]"
                        for ls in lists:
                            ret_ += "\n{}" + ls
                        cl.sendMessage(msg.to, str(ret_))
                elif msg.text.lower().startswith("stealname "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = cl.getContact(ls)
                            cl.sendMessage(msg.to, "[ Display Name ]\n" + contact.displayName)
                elif msg.text.lower().startswith("stealbio "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = cl.getContact(ls)
                            sendTextTemplate(msg.to, "[ Status Message ]\n{}" + contact.statusMessage)
                elif msg.text.lower().startswith("stealpicture "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line.naver.jp/" + cl.getContact(ls).pictureStatus
                            cl.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("stealvideoprofile "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.cl.naver.jp/" + cl.getContact(ls).pictureStatus + "/vp"
                            cl.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("stealcover "):
                    if cl != None:
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = cl.getProfileCoverURL(ls)
                                cl.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("cloneprofile "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            contact = mention["M"]
                            break
                        try:
                            cl.cloneContactProfile(contact)
                            sendTextTemplate(msg.to, "clone member ")
                        except:
                            sendTextTemplate(msg.to, "Gagal clone member")
                elif text.lower() == 'restoreprofile':
                    try:
                        clProfile.displayName = str(myProfile["displayName"])
                        clProfile.statusMessage = str(myProfile["statusMessage"])
                        clProfile.pictureStatus = str(myProfile["pictureStatus"])
                        cl.updateProfileAttribute(8, clProfile.pictureStatus)
                        cl.updateProfile(clProfile)
                        sendTextTemplate(msg.to, "restore profile ")
                    except:
                        sendTextTemplate(msg.to, "Gagal restore profile")

                elif msg.text.lower().startswith("mimicadd "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            settings["mimic"]["target"][target] = True
                            sendTextTemplate(msg.to,"Target ditambahkan!")
                            break
                        except:
                            sendTextTemplate(msg.to,"Added Target Fail !")
                            break
                elif msg.text.lower().startswith("mimicdel "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del settings["mimic"]["target"][target]
                            sendTextTemplate(msg.to,"Target dihapuskan!")
                            break
                        except:
                            sendTextTemplate(msg.to,"Deleted Target Fail !")
                            break
                elif text.lower() == 'mimiclist':
                    if settings["mimic"]["target"] == {}:
                        sendTextTemplate(msg.to,"Tidak Ada Target")
                    else:
                        mc = "╔══[ Mimic List ]"
                        for mi_d in settings["mimic"]["target"]:
                            mc += "\n╠ "+cl.getContact(mi_d).displayName
                        sendTextTemplate(msg.to,mc + "\n╚══[ Finish ]")
                elif text.lower() == 'me':
                       if msg.toType == 2:
                                contact = cl.getProfile()
                                mids = [contact.mid]
                                status = cl.getContact(sender)                             	
                                data = {
  "contents": [
    {
      "hero": {
       "aspectMode": "cover",
       "aspectRatio": "4:4",
       "type": "image",
       "url": "https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus),
       "size": "full",
       "align": "center",
      },
      "styles": {
        "body": {
          "backgroundColor": "#7D00C1"
        },
        "footer": {
          "backgroundColor": "#7D00C1"
        },
        "header": {
          "backgroundColor": "#7D00C1"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "contents": [
              {
                "contents": [
                  {
                    "type": "text",
                    "text": "{}".format(status.displayName),
                    "size": "xl",
                    "wrap": True,
                    "weight": "bold",
                    "color": "#FFAD00",
                    "align": "center"               
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },      
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [          
          {
            "type": "text",
            "text": "SELFBOT",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#81FF00",
            "align": "center"           
          }
        ]
      }
    }
  ],
  "type": "carousel"
}
                                cl.postFlex(to, data)
                elif "mimic" in msg.text.lower():
                    sep = text.split(" ")
                    mic = text.replace(sep[0] + " ","")
                    if mic == "on":
                        if settings["mimic"]["status"] == False:
                            settings["mimic"]["status"] = True
                            sendTextTemplate(msg.to,"Reply Message on")
                    elif mic == "off":
                        if settings["mimic"]["status"] == True:
                            settings["mimic"]["status"] = False
                            sendTextTemplate(msg.to,"Reply Message off")
                elif "youtube" in msg.text.lower():
                    if msg.toType == 2:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    me = best.url
                                    data = {
                                        "type": "flex",
                                        "altText": "YOUTUBE",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#FFFFFF"
    },
    "footer": {
      "backgroundColor": "#FF0000"
    }
  },
  "type": "bubble",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSgekIeIdfny8Bgr-WBIhhZgecUBZKyE89-u_SdB6Z2P-XNPdaVXhrSL1o",
            "type": "image"
          },
          {
            "type": "separator",
            "color": "#C0C0C0"
          },
          {
            "text": "YOUTUBE\nVIDEOS\nLOADING...\n\nPLAY",
            "size": "sm",
            "color": "#7D00C1",
            "wrap": True,
            "weight": "bold",
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#C0C0C0"
      },
      {
        "contents": [
          {
            "text": "JUDUL\n " + vid.title + " ?",
            "size": "xs",
            "align": "center",
            "color": "#7D00C1",
            "wrap": True,
            "weight": "bold",
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "vertical"
      },
      {
        "type": "separator",
        "color": "#C0C0C0"
      },
      {
        "contents": [
          {
            "contents": [
              {
                "url": "https://media2.giphy.com/media/13Nc3xlO1kGg3S/100.webp?cid=19f5b51a5c7364c358654a44730cc489",
                "type": "icon",
                "size": "md"
              },
              {
                "text": "Author : " + str(vid.author),
                "size": "sm",
                "margin": "none",
                "color": "#6F00FF",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "url": "https://media2.giphy.com/media/13Nc3xlO1kGg3S/100.webp?cid=19f5b51a5c7364c358654a44730cc489",
                "type": "icon",
                "size": "md"
              },
              {
                "text": "Duration : " + str(vid.duration),
                "size": "sm",
                "margin": "none",
                "color": "#6F00FF",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "url": "https://media2.giphy.com/media/13Nc3xlO1kGg3S/100.webp?cid=19f5b51a5c7364c358654a44730cc489",
                "type": "icon",
                "size": "md"
              },
              {
                "text": "Likes : " + str(vid.likes),
                "size": "sm",
                "margin": "none",
                "color": "#6F00FF",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "url": "https://media2.giphy.com/media/13Nc3xlO1kGg3S/100.webp?cid=19f5b51a5c7364c358654a44730cc489",
                "type": "icon",
                "size": "md"
              },
              {
                "text": "Rating : " + str(vid.rating),
                "size": "sm",
                "margin": "none",
                "color": "#6F00FF",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  },
  "footer": {
      "type": "box",
      "layout": "vertical",
      "contents": [{
          "type": "box",
          "layout": "horizontal",
          "contents": [{
              "type": "button",
              "flex": 2,
              "style": "primary",
              "color": "#800000",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "PLAY",
                  "uri": me
              }
          }, {
              "flex": 3,
              "type": "button",
              "style": "primary",
              "color": "#800000",
              "margin": "sm",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "YOUTUBE",
                  "uri": search_url
              }
          }]
      }]
  }
}
}
                                cl.postTemplate(to, data)
                                cl.sendVideoWithURL(msg.to, me)
                            except Exception as e:
                                cl.sendMessage(msg.to,str(e))
                elif "mp4" in msg.text.lower():
                    if msg.toType == 2:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    me = best.url
                                cl.sendVideoWithURL(msg.to, me)
                            except Exception as e:
                                cl.sendMessage(msg.to,str(e))
                elif "mp3" in msg.text.lower():
                    if msg.toType == 2:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    me = best.url
                                cl.sendAudioWithURL(msg.to, me)
                            except Exception as e:
                                cl.sendMessage(msg.to,str(e))
                elif msg.text.lower().startswith("tagremot: "):
                            	separate = msg.text.split(":")
                            	number = msg.text.replace(separate[0] + ":"," ")
                            	groups = cl.getGroupIdsJoined()
                            	gid = groups[int(number)-1]                                                            
                            	group = cl.getGroup(gid)                                                            
                            	nama = [contact.mid for contact in group.members]
                            	k = len(nama)//19
                    	        for a in range(k+1):
                            		txt = u''
                    		        s=0
                            		b=[]
                            		for i in group.members[a*19 : (a+1)*19]:
                            			b.append(i.mid)
                            		RmentionMembers(gid, b)                            
                    		        sendTextTemplate(msg.to, "Berhasil Mention Member di Group: \n " + str(group.name))
                elif "memberpicture" in msg.text.lower():
                    if msg.toType == 2:
                                  kontak = cl.getGroup(to)
                                  group = kontak.members
                                  picall = []
                                  for ids in group:
                                    if len(picall) >= 400:
                                      pass
                                    else:
                                      picall.append({
                                        "imageUrl": "https://os.line.naver.jp/os/p/{}".format(ids.mid),
                                        "action": {
                                          "type": "uri",
                                          "uri": "http://line.me/ti/p/~@cob0606n"
                                          }
                                        }
                                      )
                                  k = len(picall)//10
                                  for aa in range(k+1):
                                    data = {
                                      "type": "template",
                                      "altText": "{}".format(cl.getProfile().displayName),
                                      "template": {
                                        "type": "image_carousel",
                                        "columns": picall[aa*10 : (aa+1)*10]
                                      }
                                    }
                                    cl.postTemplate(to, data)
                elif "gettoken" in msg.text.lower():
                    if msg.toType == 2:
                                lists = {"result": [{"name": "Chrome 1\n(CHROMEOS)",},{"name": "Ios 1\n(ISOPAD)",},{"name": "Win 1\n(DESKTOPWIN)",}]}
                                if lists["result"] != []:
                                        ret_ = []
                                        for fn in lists["result"]:
                                                if len(ret_) >= 20:
                                                    pass
                                                else:
                                                    ret_.append({
                                                            "title": "{}".format(fn["name"]),
                                                            "text": "ketik Sesuai ketikan di atas",
                                                            "actions": [
                                                                {
                                                                    "type": "uri",
                                                                    "label": "CREATOR",
                                                                    "uri": "http://line.me/ti/p/~@cob0606n",
                                                                }
                                                            ]
                                                        }
                                                    )
                                        k = len(ret_)//10
                                        for aa in range(k+1):
                                            data = {
                                                    "type": "template",
                                                    "altText": "Token",
                                                    "template": {
                                                        "type": "carousel",
                                                        "columns": ret_[aa*10 : (aa+1)*10]
                                                    }
                                                }
                                            cl.postTemplate(to, data)

                elif msg.text.lower().startswith("chrome"):
                             separate = msg.text.split(" ")
                             jmlh = int(separate[1])
                             for x in range(jmlh):
                                 Headers1.update({'x-lpqs' : '/api/v4/TalkService.do'})
                                 transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4/TalkService.do')
                                 transport.setCustomHeaders(Headers1)
                                 protocol = TCompactProtocol.TCompactProtocol(transport)
                                 client = LineService.Client(protocol)
                                 qr = client.getAuthQrcode(keepLoggedIn=1, systemName=connect1)
                                 link = "line://au/q/" + qr.verifier
                                 print(link)
                                 sendTextTemplate(msg.to,"Starting white true")
                                 sendTextTemplate(msg.to,"Except")
                                 cl.sendMessage(msg.to,str(link))
                                 Headers1.update({"x-lpqs" : '/api/v4/TalkService.do', 'X-Line-Access': qr.verifier})
                                 json.loads(requests.session().get('https://gd2.line.naver.jp/Q', headers=Headers1).text)
                                 Headers1.update({'x-lpqs' : '/api/v4p/rs'})
                                 transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4p/rs')
                                 transport.setCustomHeaders(Headers1)
                                 protocol = TCompactProtocol.TCompactProtocol(transport)
                                 client = LineService.Client(protocol)
                                 req = LoginRequest()
                                 req.type = 1
                                 req.verifier = qr.verifier
                                 req.e2eeVersion = 1
                                 res = client.loginZ(req)
                                 print('\n')
                                 print(res.authToken)
                             else:
                                 sendTextTemplate(msg.to, "The bot has been mmade with DPKheaders")
                                 cl.sendMessage(msg.to,str(res.authToken))
                elif msg.text.lower().startswith("win"):
                             separate = msg.text.split(" ")
                             jmlh = int(separate[1])
                             for x in range(jmlh):
                                 Headers2.update({'x-lpqs' : '/api/v4/TalkService.do'})
                                 transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4/TalkService.do')
                                 transport.setCustomHeaders(Headers2)
                                 protocol = TCompactProtocol.TCompactProtocol(transport)
                                 client = LineService.Client(protocol)
                                 qr = client.getAuthQrcode(keepLoggedIn=1, systemName=connect2)
                                 link = "line://au/q/" + qr.verifier
                                 print(link)
                                 sendTextTemplate(msg.to,"Starting white true")
                                 sendTextTemplate(msg.to,"Except")
                                 cl.sendMessage(msg.to,str(link))
                                 Headers2.update({"x-lpqs" : '/api/v4/TalkService.do', 'X-Line-Access': qr.verifier})
                                 json.loads(requests.session().get('https://gd2.line.naver.jp/Q', headers=Headers2).text)
                                 Headers2.update({'x-lpqs' : '/api/v4p/rs'})
                                 transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4p/rs')
                                 transport.setCustomHeaders(Headers2)
                                 protocol = TCompactProtocol.TCompactProtocol(transport)
                                 client = LineService.Client(protocol)
                                 req = LoginRequest()
                                 req.type = 1
                                 req.verifier = qr.verifier
                                 req.e2eeVersion = 1
                                 res = client.loginZ(req)
                                 print('\n')
                                 print(res.authToken)
                             else:
                                 sendTextTemplate(msg.to, "The bot has been mmade with ARIFISTIFIKheaders")
                                 cl.sendMessage(msg.to,str(res.authToken))
                elif msg.text.lower().startswith("ios"):
                             separate = msg.text.split(" ")
                             jmlh = int(separate[1])
                             for x in range(jmlh):
                                 Headers3.update({'x-lpqs' : '/api/v4/TalkService.do'})
                                 transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4/TalkService.do')
                                 transport.setCustomHeaders(Headers3)
                                 protocol = TCompactProtocol.TCompactProtocol(transport)
                                 client = LineService.Client(protocol)
                                 qr = client.getAuthQrcode(keepLoggedIn=1, systemName=connect3)
                                 link = "line://au/q/" + qr.verifier
                                 print(link)
                                 sendTextTemplate(msg.to,"Starting white true")
                                 sendTextTemplate(msg.to,"Except")
                                 cl.sendMessage(msg.to,str(link))
                                 Headers3.update({"x-lpqs" : '/api/v4/TalkService.do', 'X-Line-Access': qr.verifier})
                                 json.loads(requests.session().get('https://gd2.line.naver.jp/Q', headers=Headers3).text)
                                 Headers3.update({'x-lpqs' : '/api/v4p/rs'})
                                 transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4p/rs')
                                 transport.setCustomHeaders(Headers3)
                                 protocol = TCompactProtocol.TCompactProtocol(transport)
                                 client = LineService.Client(protocol)
                                 req = LoginRequest()
                                 req.type = 1
                                 req.verifier = qr.verifier
                                 req.e2eeVersion = 1
                                 res = client.loginZ(req)
                                 print('\n')
                                 print(res.authToken)
                             else:
                                 sendTextTemplate(msg.to, "The bot has been mmade with DPKTEAMheader")
                                 cl.sendMessage(msg.to,str(res.authToken))
                elif msg.text.lower().startswith("ytsearch "):
                    if msg.toType == 2:
                                sep = text.split(" ")
                                search = text.replace(sep[0] + " ","")
                                r = requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=10&q={}&type=video&key=AIzaSyAF-_5PLCt8DwhYc7LBskesUnsm1gFHSP8".format(str(search)))
                                data = r.text
                                a = json.loads(data)
                                if a["items"] != []:
                                    ret_ = []
                                    yt = []
                                    for music in a["items"]:
                                        ret_.append({
                                            "type": "bubble",
                                            "styles": {
                                                "header": {
                                                    "backgroundColor": "#0000FF"
                                                },
                                                "body": {
                                                   "backgroundColor": "#7D00C1",
                                                   "separator": True,
                                                   "separatorColor": "#FF0000"
                                                },
                                                "footer": {
                                                    "backgroundColor": "#FF7F50",
                                                    "separator": True,
                                                   "separatorColor": "#FF0000"
                                               }
                                            },
                                            "hero": {
                                                "type": "image",
                                                "url": "https://i.ytimg.com/vi/{}/maxresdefault.jpg".format(music['id']['videoId']),
                                                "size": "full",
                                                "aspectRatio": "20:13",
                                                "aspectMode": "cover",
                                                "action": {
                                                    "type": "uri",
                                                    "uri": "line://nv/profilePopup/mid=u26379f895f9a0af38a66dbc0e76f663c"
                                                }
                                            },
                                            "body": {
                                                "type": "box",
                                                "spacing": "md",
                                                "layout": "horizontal",
                                                "contents": [{
                                                    "type": "box",
                                                    "spacing": "none",
                                                    "flex": 1,
                                                    "layout": "vertical",
                                                    "contents": [{
                                                        "type": "image",
                                                        "url": "https://cdn2.iconfinder.com/data/icons/social-icons-circular-color/512/youtube-512.png",
                                                        "aspectMode": "cover",
                                                        "gravity": "bottom",
                                                        "size": "sm",
                                                        "aspectRatio": "1:1",
                                                        "action": {
                                                          "type": "uri",
                                                          "uri": "https://www.youtube.com/watch?v=%s" % music['id']['videoId']
                                                        }
                                                    }]
                                                }, {
                                                    "type": "separator",
                                                    "color": "#FF0000"
                                                }, {
                                                    "type": "box",
                                                    "contents": [{
                                                        "type": "text",
                                                        "text": "JUDUL",
                                                        "color": "#00BFFF",
                                                        "size": "md",
                                                        "weight": "bold",
                                                        "flex": 1,
                                                        "gravity": "top"
                                                    }, {
                                                        "type": "separator",
                                                        "color": "#FF0000"
                                                    }, {
                                                        "type": "text",
                                                        "text": "%s" % music['snippet']['title'],
                                                        "color": "#00FF00",
                                                        "size": "sm",
                                                        "weight": "bold",
                                                        "flex": 3,
                                                        "wrap": True,
                                                        "gravity": "top"
                                                    }],
                                                    "flex": 2,
                                                    "layout": "vertical"
                                                }]
                                            },
                                            "footer": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [{
                                                    "type": "box",
                                                    "layout": "horizontal",
                                                    "contents": [{
                                                        "type": "button",
                                                        "flex": 2,
                                                        "style": "primary",
                                                        "color": "#1E90FF",
                                                        "height": "sm",
                                                        "action": {
                                                            "type": "uri",
                                                            "label": "Youtube",
                                                            "uri": "https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                                                        }
                                                    }, {
                                                        "flex": 3,
                                                        "type": "button",
                                                        "margin": "sm",
                                                        "style": "primary",
                                                        "color": "#7B68EE",
                                                        "height": "sm",
                                                        "action": {
                                                            "type": "uri",
                                                            "label": "Mp3",
                                                            "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=mp3%20https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                                                        }
                                                    }]
                                                }, {
                                                    "type": "button",
                                                    "margin": "sm",
                                                    "style": "primary",
                                                    "color": "#191970",
                                                    "height": "sm",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Mp4",
                                                        "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=youtubemp4%20https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                                                    }
                                                }]
                                            }
                                        }
                                    )
                                        yt.append('https://www.youtube.com/watch?v=' +music['id']['videoId'])
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                            "type": "flex",
                                            "altText": "Youtube",
                                            "contents": {
                                                "type": "carousel",
                                                "contents": ret_[aa*10 : (aa+1)*10]
                                            }
                                        }
                                        cl.postTemplate(to, data)
                elif text.lower() == 'groupcreator':
                    group = cl.getGroup(to)
                    GS = group.creator.mid
                    cl.sendContact(to, GS)
                elif text.lower() == 'groupid':
                    gid = cl.getGroup(to)
                    cl.sendMessage(to, "[ID Group : ]\n" + gid.id)
                elif text.lower() == 'grouppicture':
                    group = cl.getGroup(to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    cl.sendImageWithURL(to, path)
                elif text.lower() == 'groupname':
                    gid = cl.getGroup(to)
                    cl.sendMessage(to, "[Nama Group : ]\n" + gid.name)
                elif text.lower() == 'groupticket':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = cl.reissueGroupTicket(to)
                            cl.sendMessage(to, "[ Group Ticket ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                        else:
                            cl.sendMessage(to, "Grup qr tidak terbuka silahkan buka terlebih dahulu dengan perintah {}openqr".format(str(settings["keyCommand"])))
                elif text.lower() == 'groupticket on':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            cl.sendMessage(to, "Grup qr sudah terbuka")
                        else:
                            group.preventedJoinByTicket = False
                            cl.updateGroup(group)
                            cl.sendMessage(to, "membuka grup qr")
                elif text.lower() == 'groupticket off':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            cl.sendMessage(to, "Grup qr sudah tertutup")
                        else:
                            group.preventedJoinByTicket = True
                            cl.updateGroup(group)
                            cl.sendMessage(to, "menutup grup qr")
                elif text.lower() == 'groupinfo':
                    group = cl.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Tidak ditemukan"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "Tertutup"
                        gTicket = "Tidak ada"
                    else:
                        gQr = "Terbuka"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "╔══[ Group Info ]"
                    ret_ += "\n╠ Nama Group : {}".format(str(group.name))
                    ret_ += "\n╠ ID Group : {}".format(group.id)
                    ret_ += "\n╠ Pembuat : {}".format(str(gCreator))
                    ret_ += "\n╠ Jumlah Member : {}".format(str(len(group.members)))
                    ret_ += "\n╠ Jumlah Pending : {}".format(gPending)
                    ret_ += "\n╠ Group Qr : {}".format(gQr)
                    ret_ += "\n╠ Group Ticket : {}".format(gTicket)
                    ret_ += "\n╚══[ Group Info ]"
                    cl.sendMessage(to, str(ret_))
                    cl.sendImageWithURL(to, path)
                elif text.lower() == 'groupmemberlist':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        ret_ = "╔══[ Member List ]"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n╠ {}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n╚══[ Total {} ]".format(str(len(group.members)))
                        sendTextTemplate(to, str(ret_))
                elif text.lower() == 'grouplist':
                        groups = cl.groups
                        ret_ = "╔══[ Group List ]"
                        no = 0 + 1
                        for gid in groups:
                            group = cl.getGroup(gid)
                            ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n╚══[ Total {} Groups ]".format(str(len(groups)))
                        cl.sendMessage(to, str(ret_))
                elif text.lower() == 'notif on':
                   if settings["notifikasi"] == True:
                       if settings["lang"] == "JP":
                           sendTextTemplate(msg.to,"notif mode on")
                   else:
                       settings["notifikasi"] = True
                       if settings["lang"] == "JP":
                           sendTextTemplate(msg.to,"notif mode on")

                elif text.lower() == 'notif off':
                   if settings["notifikasi"] == False:
                       if settings["lang"] == "JP":
                          sendTextTemplate(msg.to,"notif mode off")
                   else: 
                       settings["notifikasi"] = False
                       if settings["lang"] == "JP":
                           sendTextTemplate(msg.to,"notif mode off")
                elif text.lower() == 'tag':
                            if msg.toType == 0:
                                sendMention(to, to, "", "")
                            elif msg.toType == 2:
                                group = cl.getGroup(to)
                                midMembers = [contact.mid for contact in group.members]
                                midSelect = len(midMembers)//20
                                for mentionMembers in range(midSelect+1):
                                    no = 0
                                    ret_ = "╔══[ Mention Members ]"
                                    dataMid = []
                                    for dataMention in group.members[mentionMembers*20 : (mentionMembers+1)*20]:
                                        dataMid.append(dataMention.mid)
                                        no += 1
                                        ret_ += "\n╠ {}. @!".format(str(no))
                                    ret_ += "\n╚══[ Total {} Members]".format(str(len(dataMid)))
                                    cl.sendMention(msg.to, ret_, dataMid)
                elif text.lower() == 'changepictureprofile':
                            settings["changePicture"] = True
                            sendTextTemplate(to, "Silahkan kirim gambarnya")
                elif text.lower() == 'changegrouppicture':
                            if msg.toType == 2:
                                if to not in settings["changeGroupPicture"]:
                                    settings["changeGroupPicture"].append(to)
                                sendTextTemplate(to, "Silahkan kirim gambarnya")
                elif text.lower() == 'lurking on':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read['readPoint']:
                            try:
                                del read['readPoint'][msg.to]
                                del read['readMember'][msg.to]
                                del read['readTime'][msg.to]
                            except:
                                pass
                            read['readPoint'][msg.to] = msg.id
                            read['readMember'][msg.to] = ""
                            read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                            read['ROM'][msg.to] = {}
                            with open('read.json', 'w') as fp:
                                json.dump(read, fp, sort_keys=True, indent=4)
                                sendTextTemplate(msg.to,"Lurking already on")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                            pass
                        read['readPoint'][msg.to] = msg.id
                        read['readMember'][msg.to] = ""
                        read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        read['ROM'][msg.to] = {}
                        with open('read.json', 'w') as fp:
                            json.dump(read, fp, sort_keys=True, indent=4)
                            sendTextTemplate(msg.to, "Set reading point:\n" + readTime)
                            
                elif text.lower() == 'lurking off':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to not in read['readPoint']:
                        sendTextTemplate(msg.to,"Lurking already off")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                              pass
                        sendTextTemplate(msg.to, "Delete reading point:\n" + readTime)
    
                elif text.lower() == 'lurking reset':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read["readPoint"]:
                        try:
                            del read["readPoint"][msg.to]
                            del read["readMember"][msg.to]
                            del read["readTime"][msg.to]
                        except:
                            pass
                        sendTextTemplate(msg.to, "Reset reading point:\n" + readTime)
                    else:
                        sendTextTemplate(msg.to, "Lurking belum diaktifkan ngapain di reset?")
                        
                elif text.lower() == 'lurking':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if receiver in read['readPoint']:
                        if read["ROM"][receiver].items() == []:
                            cl.sendMessage(receiver,"[ Reader ]:\nNone")
                        else:
                            chiya = []
                            for rom in read["ROM"][receiver].items():
                                chiya.append(rom[1])
                            cmem = cl.getContacts(chiya) 
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = '[ Reader ]:\n'
                        for x in range(len(cmem)):
                            xname = str(cmem[x].displayName)
                            pesan = ''
                            pesan2 = pesan+"@c\n"
                            xlen = str(len(zxc)+len(xpesan))
                            xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                            zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                            zx2.append(zx)
                            zxc += pesan2
                        text = xpesan+ zxc + "\n[ Lurking time ]: \n" + readTime
                        try:
                            cl.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                        except Exception as error:
                            print (error)
                        pass
                    else:
                        sendTextTemplate(receiver,"ketik[ lurking on ]dulu peak lu")

                elif text.lower() == 'sider on':
                    try:
                        del cctv['point'][msg.to]
                        del cctv['sidermem'][msg.to]
                        del cctv['cyduk'][msg.to]
                    except:
                        pass
                    cctv['point'][msg.to] = msg.id
                    cctv['sidermem'][msg.to] = ""
                    cctv['cyduk'][msg.to]=True 
                    settings["Sider"] = True
                    sendTextTemplate(msg.to,"SIDER SUDAH ON")

                elif text.lower() == 'sider off':
                    if msg.to in cctv['point']:
                       cctv['cyduk'][msg.to]=False
                       settings["Sider"] = False
                       sendTextTemplate(msg.to,"SIDER SUDAH OFF")
                    else:
                        sendTextTemplate(msg.to,"SIDER SUDAH OFF")

                elif text.lower() == 'kalender':
                    tz = pytz.timezone("Asia/Makassar")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    sendTextTemplate(msg.to, readTime)                 
                elif "checkdate" in msg.text.lower():
                    sep = msg.text.split(" ")
                    tanggal = msg.text.replace(sep[0] + " ","")
                    r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                    data=r.text
                    data=json.loads(data)
                    ret_ = ""
                    ret_ += "Date Of Birth : {}".format(str(data["data"]["lahir"]))
                    ret_ += "\nAge : {}".format(str(data["data"]["usia"]))
                    ret_ += "\nBirthday : {}".format(str(data["data"]["ultah"]))
                    ret_ += "\nZodiak : {}".format(str(data["data"]["zodiak"]))
                    ret_ += ""
                    sendTextTemplate(to, str(ret_))
            elif msg.contentType == 7:
                if settings["checkSticker"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    ret_ = ""
                    ret_ += "STICKER ID : {}".format(stk_id)
                    ret_ += "\nSTICKER PACKAGES ID : {}".format(pkg_id)
                    ret_ += "\nSTICKER VERSION : {}".format(stk_ver)
                    ret_ += "\nSTICKER URL : line://shop/detail/{}".format(pkg_id)
                    ret_ += ""
                    cl.sendMessage(to, str(ret_))

            elif msg.contentType == 1:
                    if settings["changePicture"] == True:
                        path = cl.downloadObjectMsg(msg_id)
                        settings["changePicture"] = False
                        cl.updateProfilePicture(path)
                        sendTextTemplate(to, "mengubah foto profile")
                    if msg.toType == 2:
                        if to in settings["changeGroupPicture"]:
                            path = cl.downloadObjectMsg(msg_id)
                            settings["changeGroupPicture"].remove(to)
                            cl.updateGroupPicture(to, path)
                            sendTextTemplate(to, "mengubah foto group")

        if op.type == 26 or op.type == 25:
            print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                if settings["autoRead"] == True:
                    cl.sendChatChecked(to, msg_id)
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
                    text = msg.text
                    if text is not None:
                        cl.sendMessage(msg.to,text)
                if msg.contentType == 16:
                    if msg.toType in (2,1,0):
                        purl = msg.contentMetadata["postEndUrl"].split('userMid=')[1].split('&postId=')
                        adw = cl.likePost(purl[0], purl[1], random.choice([1001,1002,1003,1004,1005]))
                        adws = cl.createComment(purl[0], purl[1], settings["commentPost"])
                        sendTextTemplate(to, "AUTO LIKE SUCCES")
                if msg.contentType == 0 and sender not in clMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        group = cl.getGroup(to)
                        for mention in mentionees:
                            if clMid in mention["M"]:
                            	if settings["detectMention"] == True:
                                    data = {
                                                        "type": "flex",
                                                        "altText": "you kickout from group",
                                                        "contents": {
                  "styles": {
                    "body": {
                      "backgroundColor": "#0000CD"
                    }
                  },
                  "type": "bubble",
                  "body": {
                    "contents": [
                      {
                        "contents": [
                          {
                            "contents": [
                              {
                                "text": settings["autoResponMessage"],
                                "size": "md",
                                "margin": "none",
                                "color": "#FFFF00",
                                "wrap": True,
                                "weight": "bold",
                               "type": "text"
                              }
                            ],
                            "type": "box",
                            "layout": "baseline"
                          }
                        ],
                        "type": "box",
                        "layout": "vertical"
                      }
                    ],
                    "type": "box",
                    "spacing": "md",
                    "layout": "vertical"
                  }
                }
                }
                                    cl.postTemplate(to, data)
                            	break

        if op.type == 17:
           print ("MEMBER JOIN TO GROUP")
           if settings["notifikasi"] == True:
             if op.param2 in clMID:
                 return
             ginfo = cl.getGroup(op.param1)
             contact = cl.getContact(op.param2)
             image = "http://dl.profile.line.naver.jp/" + contact.pictureStatus
             data = {
                                "type": "flex",
                                "altText": "DPK",
                                "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#7D00C1"
    },
    "footer": {
      "backgroundColor": "#7D00C1"
    }
  },
  "type": "bubble",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "text":" Selamat datang  dan selamat bergabung\nBUDAYAKAN CEK NOT 🙏\nSemoga betah 🙏 🙏 ".format(cl.getContact(op.param2).displayName),
            "size": "sm",
            "color": "#00FF00",
            "wrap": True,
            "type": "text",
            "align": "center"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(op.param2).pictureStatus),
            "type": "image",
            "size": "full"
          }       
        ],
        "type": "box",
        "layout": "horizontal"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  },
  "footer": {
      "type": "box",
      "layout": "vertical",
      "contents": [{
          "type": "box",
          "layout": "horizontal",
          "flex": 2,
          "contents": [{
              "type": "button",
              "style": "secondary",
              "color": "#00FF00",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "CREATOR",
                  "uri": "http://line.me/ti/p/~@cob0606n"
              }
          }]
      }]
  }
}
}
             cl.postTemplate(op.param1, data)
             #cl.sendMessage(op.param1,"Halo... " + cl.getContact(op.param2).displayName + "\nSelamat datang di\n💎 " + str(ginfo.name) + " 💎" + "\n jangan lupa ngenot \n& Semoga betah ya😃")
             #cl.sendImageWithURL(op.param1,image)

        if op.type == 15:
           print ("MEMBER LEAVE TO GROUP")
           if settings["notifikasi"] == True:
             if op.param2 in clMID:
                 return
             ginfo = cl.getGroup(op.param1)
             contact = cl.getContact(op.param2)
             image = "http://dl.profile.line.naver.jp/" + contact.pictureStatus
             data = {
                                "type": "flex",
                                "altText": "DPK",
                                "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#7D00C1"
    },
    "footer": {
      "backgroundColor": "#7D00C1"
    }
  },
  "type": "bubble",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "text":"Bye bye sob\n\nsee you next time\n\n{}".format(cl.getContact(op.param2).displayName),
            "size": "sm",
            "color": "#00FF00",
            "wrap": True,
            "type": "text",
            "align": "center"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(op.param2).pictureStatus),
            "type": "image",
            "size": "full"
          }       
        ],
        "type": "box",
        "layout": "horizontal"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  },
  "footer": {
      "type": "box",
      "layout": "vertical",
      "contents": [{
          "type": "box",
          "layout": "horizontal",
          "flex": 2,
          "contents": [{
              "type": "button",
              "style": "secondary",
              "color": "#00FF00",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "CREATOR",
                  "uri": "http://line.me/ti/p/~@cob0606n"
              }
          }]
      }]
  }
}
}
             cl.postTemplate(op.param1, data)

        if op.type == 55:
            print ("[ 55 ] NOTIFIED READ MESSAGE")
            try:
                if cctv['cyduk'][op.param1]==True:
                    if op.param1 in cctv['point']:
                        Name = cl.getContact(op.param2).displayName
                        if Name in cctv['sidermem'][op.param1]:
                            pass
                        else:
                            cctv['sidermem'][op.param1] += "\nâ¢ " + Name
                            if " " in Name:
                                nick = Name.split(' ')
                                if len(nick) == 2:
                                    Camera(op.param1, Name)
                                    time.sleep(0.2)
                                else:
                                    Camera(op.param1, Name)
                                    time.sleep(0.2)
                            else:
                                Camera(op.param1, Name)
                                time.sleep(0.2)
                    else:
                        pass
                else:
                    pass
            except:
                pass


        if op.type == 55:
            print ("[ 55 ] NOTIFIED READ MESSAGE")
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
    except Exception as error:
        logError(error)

while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                clBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
