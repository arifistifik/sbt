from thrift.protocol import TCompactProtocol
from thrift.transport import THttpClient
from akad.ttypes import IdentityProvider, LoginResultType, LoginRequest, LoginType

import json, requests, livejson, LineService

def loggedIn(func):
    def checkLogin(*args, **kwargs):
        if args[0].isLogin:
            return func(*args, **kwargs)
        else:
            args[0].callback.other('You want to call the function, you must login to LINE')
    return checkLogin

class getToken:
	isLogin = False

	def __init__(self):
		self.isLogin = True

	@loggedIn
	def DESKTOPMAC(self):
	    Headers = {
	    'User-Agent': "Line/8.3.2",
	    'X-Line-Application': "DESKTOPMAC\t5.10.0\tARIFISTIFIK\tTools\t10.13.2",
	    "x-lal": "ja-US_US",
	    }
	    return Headers

	@loggedIn
	def DESKTOPWIN(self):
	    Headers = {
	    'User-Agent': "Line/8.3.2",
	    'X-Line-Application': "DESKTOPWIN\t5.10.0\tARIFISTIFIK\tTools\t10.13.2",
	    "x-lal": "ja-US_US",
	    }
	    return Headers

	@loggedIn
	def IOSIPAD(self):
	    Headers = {
	    'User-Agent': "Line/8.3.2",
	    'X-Line-Application': "IOSIPAD\t8.14.2\tARIFISTIFIK\tTools\t11.2.5",
	    "x-lal": "ja-US_US",
	    }
	    return Headers

	@loggedIn
	def CHROMEOS(self):
	    Headers = {
	    'User-Agent': "Line/8.3.2",
	    'X-Line-Application': "CHROMEOS\t2.1.5\tARIFISTIFIK\tTools\t11.2.5",
	    "x-lal": "ja-US_US",
	    }
	    return Headers

	@loggedIn
	def WIN10(self):
	    Headers = {
	    'User-Agent': "Line/8.3.2",
	    'X-Line-Application': "WIN10\t5.5.5\tARIFISTIFIK\tTools\t11.2.5",
	    "x-lal": "ja-US_US",
	    }
	    return Headers

	@loggedIn
	def token(self,to,token,msg_id,sender,nametoken):
	    try:
	        a = token
	        a.update({'x-lpqs' : '/api/v4/TalkService.do'})
	        transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4/TalkService.do')
	        transport.setCustomHeaders(a)
	        protocol = TCompactProtocol.TCompactProtocol(transport)
	        clienttoken = LineService.Client(protocol)
	        qr = clienttoken.getAuthQrcode(keepLoggedIn=1, systemName='ARIFISTIFIK')
	        link = "line://au/q/" + qr.verifier
	        #self.sendReplyMessage(msg_id, to, "Click This Link Only For 2 Minute :)\n\n{}".format(link))
	        data = {
	        	"type": "template",
	        	"altText": "Token",
	        	"template": {
	        		"type": "buttons",
	        		"title": "Token %s" % nametoken,
	        		"text": "Click This Button\nOnly For 2 Minutes",
	        		"actions": [
	        			{
	        				"type": "uri",
	        				"label": "Click Me",
	        				"uri": link
	        			},
	        			{
	        				"type": "uri",
	        				"label": "Link ?",
	        				"uri": 'line://app/1603968955-ORWb9RdY/?type=text&text=%s' % link
	        			}
	        		]
	        	}
	        }
	        self.postTemplate(to, data)
	        a.update({"x-lpqs" : '/api/v4/TalkService.do', 'X-Line-Access': qr.verifier})
	        json.loads(requests.session().get('https://gd2.line.naver.jp/Q', headers=a).text)
	        a.update({'x-lpqs' : '/api/v4p/rs'})
	        transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4p/rs')
	        transport.setCustomHeaders(a)
	        protocol = TCompactProtocol.TCompactProtocol(transport)
	        clienttoken = LineService.Client(protocol)
	        req = LoginRequest()
	        req.type = 1
	        req.verifier = qr.verifier
	        req.e2eeVersion = 1
	        res = clienttoken.loginZ(req)
	        try:
	        	settings = livejson.File('setting.json', True, True, 4)
	        	settings['token']['token'] = res.authToken
	        	settings['token']['status'] = True
	        	self.sendMessage(to, 'Success get your token,\nCek Your Private Chat')
	        except Exception as e:
	            self.sendMessage(to, str(e))
	    except Exception as error:
	        self.sendMessage(to, "Login Bangsat")
	        self.sendMessage(to, str(error))