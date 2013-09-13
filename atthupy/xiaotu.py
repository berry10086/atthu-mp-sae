# -*- coding: utf-8 -*-
import urllib2
import urllib
import cookielib


def get_xiaotu_response(input_msg):
	url_base = 'http://166.111.120.164:8081/programd/'
	UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.71 Safari/537.36'

	"""
	cookie = cookielib.CookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
	response = opener.open(url_base)
	"""
	
	req = urllib2.Request(url_base)
	req.add_header('User-Agent', UA)
	try:
		cookie = urllib2.urlopen(req).info()['Set-cookie'].split(';')[0]
	except KeyError,e:
		cookie = urllib2.urlopen(req).info()['cookie'].split(';')[0]
#    return cookie
	uu = input_msg
	uu = urllib.quote(uu)
	uu = "string:"+uu
	uu = urllib.quote(uu)
    

	url_append = "dwr/exec/bot.getResponse?callCount=1&c0-scriptName=bot&c0-methodName=getResponse&c0-id=9518_1378899674170&c0-param0=%s&xml=true" % uu

	



	req = urllib2.Request(url_base+url_append)
	req.add_header('User-Agent', UA)
	req.add_header('cookie', cookie)

	#page = opener.open(req).read()
	page = urllib2.urlopen(req).read()
#	info = urllib2.urlopen(req).info()
	msg = page.split('"')[1].decode('unicode_escape').strip()
#	print info
	return msg

if __name__ == '__main__':
	while(1):
		msg = raw_input('input:')
		#msg = 'w'
		#msg.decode('gbk').encode('utf-8')
		print get_xiaotu_response(msg)
