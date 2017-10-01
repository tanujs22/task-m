#!/usr/bin/env python2.7
from flask import Flask, render_template
import urllib, urllib2, json
app = Flask(__name__)


@app.route('/')
def requiredID():
	url = "https://test.oppwa.com/v1/checkouts"
	data = {
		'authentication.userId' : '8a8294174b7ecb28014b9699220015cc',
		'authentication.password' : 'sy6KJsT8',
		'authentication.entityId' : '8a8294174b7ecb28014b9699220015ca',
		'amount' : '92.00',
		'currency' : 'EUR',
		'paymentType' : 'DB'
	}
	try:
		opener = urllib2.build_opener(urllib2.HTTPHandler)
		request = urllib2.Request(url, data=urllib.urlencode(data))
		request.get_method = lambda: 'POST'
		response = opener.open(request)
		result = json.loads(response.read())
		return render_template('home.html', check_id=result['id'])
	except Exception, e:
		return e;
	

if __name__ == "__main__":
		app.debug = True
		app.run()