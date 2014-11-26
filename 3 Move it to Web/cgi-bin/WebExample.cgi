#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import cgi

# enable debugging
import cgitb
cgitb.enable()

#dropbox import
import dropbox

#parse some of the stuff we get back
import json

# Create instance of FieldStorage 
form = cgi.FieldStorage()

try:
  authKey = form["authKey"].value
except:
  authKey = 0;

print "Content-type:text/html\r\n\r\n"
print '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">'
print '<html xmlns="http://www.w3.org/1999/xhtml" lang="en">'
print '<head>'
print '<meta http-equiv="Content-Type" content="text/html" />'
print '</head>'
print '<body>'

print '<h1>Hello Dropbox</h1>'

#Set up the App Secret - you get this from the developer page in your DB account:
app_key = 'hi308thvvbnghlh'  
app_secret = '9la222bag3gwp6q'

flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)

# Have the user sign in and authorize this token
authorize_url = flow.start()
print '<p>1. Go to: <h5 style="color:red">' + authorize_url + '</h5></p>'
print '<p>2. Click "Allow" (you might have to log in first)</p>'
print '<p>3. Copy the authorization code.</p>'
print '<form action="webexample.cgi" method="post">'
print '<p>Paste Authorization code here: <input type="text" name="authKey"></p>'
print '<p><input type="submit" value="Authenticate"/>'
print '</form>'

if authKey == 0 or authKey is None:
	print '<p>Enter an auth key to move forward...</p>'
else:
	access_token, user_id = flow.finish(authKey)
	#At this point we have the access token and user id, the next step is to try using the API. 
	if user_id:
		dbclient = dropbox.client.DropboxClient(access_token, locale="en-US", rest_client=None)
		userDetail = dbclient.account_info()
		print '<p>---------------------------------</p>'
		print '<p>Log in complete.</p>'
		print '<p>.................................</p>'
		print '<p>Display name: ' + userDetail['display_name'] + '</p>'
		print '<p>Email: ' + userDetail['email'] + '</p>'
		print '<p>User Id: ' + str(userDetail['uid']) + '</p>'
		print '<p>.................................</p>'

		#working with files
		#uploading a file
		testfile = open('test.txt', 'rb')
		response = dbclient.put_file('/test.txt', testfile)
		print '<p>uploaded file:', response['path'] + '</p>'
		print '<p>.................................' + '</p>'

		#retrieving the content of a folder
		folder_metadata = dbclient.metadata('/')
		print '<p>folder: ', folder_metadata['path'] + '</p>'
		print '<p>.................................</p>'

		#downloading a file
		testfile, metadata = dbclient.get_file_and_metadata('/test.txt')
		out = open('test.txt', 'wb')
		out.write(testfile.read())
		out.close()
		print '<p>downloaded file: ', metadata['path'] + '</p>'
		print '<p>.................................</p>'
	

#access_token, user_id = flow.finish(code)

print '</body>'
print '</html>'
