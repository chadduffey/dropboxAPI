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
print '<link rel="stylesheet" href="../dist/css/bootstrap.css">'
print '<link href="http://fonts.googleapis.com/css?family=Nunito:400,300|Amatic+SC|Open+Sans+Condensed:300" rel="stylesheet" type="text/css">'
print '<link rel="stylesheet" href="../css/main.css">'
print '</head>'
print '<body>'

print '<h1><img src="../img/dropbox.png" alt="Dropbox Logo"/></h1>'
print '<h1>Hello Dropbox</h1>'

#Set up the App Secret - you get this from the developer page in your DB account:
app_key = 'hi308thvvbnghlh'  
app_secret = '9la222bag3gwp6q'

flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)

# Have the user sign in and authorize this token
authorize_url = flow.start()

if authKey == 0 or authKey is None:
	print '<form action="webexample.cgi" method="post">'
	print '<p>Obtain Authorization from <font color="red"><a href="' + authorize_url + ' " target="_blank">here</a></font></p>'
	print '<p>Paste the code here: <input type="text" class="form-control" name="authKey"></p>'
	print '<p><button type="submit" class="btn btn-info" value="Authenticate">Authenticate</button>'
	print '</form>'
else:
	access_token, user_id = flow.finish(authKey)
	#At this point we have the access token and user id, the next step is to try using the API. 
	if user_id:

		dbclient = dropbox.client.DropboxClient(access_token, locale="en-US", rest_client=None)
		userDetail = dbclient.account_info()
		print '<form>'
		print '<p><span class="glyphicon glyphicon-user" aria-hidden="true"></span> Display name: ' + userDetail['display_name'] + '</p>'
		print '<p><span class="glyphicon glyphicon-envelope" aria-hidden="true"></span> Email: ' + userDetail['email'] + '</p>'
		print '<p><span class="glyphicon glyphicon-tower" aria-hidden="true"></span> User Id: ' + str(userDetail['uid']) + '</p>' 

		#working with files
		#retrieving the content of a folder
		folder_metadata = dbclient.metadata('/')
		print '<p><span class="glyphicon glyphicon-folder-open" aria-hidden="true"></span> folder: ', folder_metadata['path'] + '</p>'

		#uploading a file
		testfile = open('test.txt', 'rb')
		response = dbclient.put_file('/test.txt', testfile)
		print '<p><span class="glyphicon glyphicon-file" aria-hidden="true"></span> uploaded file: ', response['path'] + '</p>'

		#downloading a file
		testfile, metadata = dbclient.get_file_and_metadata('/test.txt')
		out = open('test.txt', 'wb')
		out.write(testfile.read())
		out.close()
		print '<p><span class="glyphicon glyphicon-file" aria-hidden="true"></span> downloaded file: ', metadata['path'] + '</p>'
		print '</form>'

#access_token, user_id = flow.finish(code)

print '</body>'
print '</html>'
