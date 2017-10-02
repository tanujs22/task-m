#!/usr/bin/env python2.7
from flask import Flask, render_template, jsonify
from flask import request as rt
from werkzeug.datastructures import CombinedMultiDict, MultiDict
import urllib, urllib2, json
app = Flask(__name__)


@app.route('/')
def requiredID():
	url = "https://test.oppwa.com/v1/checkouts"
	data = {
		'authentication.userId' : '8a8294174b7ecb28014b9699220015cc',
		'authentication.password' : 'sy6KJsT8',
		'authentication.entityId' : '8a8294174b7ecb28014b9699220015ca',
		'amount' : '11.97',
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
	except urllib2.HTTPError, e:
		return e.code;

@app.route('/formresponse')
def requestform():
	parameters = CombinedMultiDict([rt.args, rt.form])
	check_id = parameters['id']
	url = "https://test.oppwa.com/v1/checkouts/"+check_id+"/payment"
	url += '?authentication.userId=8a8294174b7ecb28014b9699220015cc'
	url += '&authentication.password=sy6KJsT8'
	url += '&authentication.entityId=8a8294174b7ecb28014b9699220015ca'
	try:
		opener = urllib2.build_opener(urllib2.HTTPHandler)
		request = urllib2.Request(url, data='')
		request.get_method = lambda: 'GET'
		response = opener.open(request)
		res = jsonify(response.read())
		print res
		return res
	except urllib2.HTTPError, e:
		return e.code;

	

if __name__ == "__main__":
		app.debug = True
		app.run()