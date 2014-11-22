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
print '<p>1. Go to: ' + authorize_url + '</p>'
print '<p>2. Click "Allow" (you might have to log in first)</p>'
print '<p>3. Copy the authorization code.</p>'
#code = raw_input("Enter the authorization code here: ").strip()
print '<form action="webexample.cgi" method="post">'
print '<p>Paste Authorization code here: <input type="text" name="authKey"></p>'
print '<p><input type="submit" value="Authenticate"/>'
print '</form>'

if authKey == 0 or authKey is None:
	print '<p>Enter an auth key to move forward...</p>'

#access_token, user_id = flow.finish(code)

print '</body>'
print '</html>'
