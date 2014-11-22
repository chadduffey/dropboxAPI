import dropbox
import json


#Set up the App Secret - you get this from the developer page in your DB account:
app_key = 'hi308thvvbnghlh'  
app_secret = '9la222bag3gwp6q'

flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)

# Have the user sign in and authorize this token
authorize_url = flow.start()
print '1. Go to: ' + authorize_url
print '2. Click "Allow" (you might have to log in first)'
print '3. Copy the authorization code.'
code = raw_input("Enter the authorization code here: ").strip()

access_token, user_id = flow.finish(code)

#At this point we have the access token and user id, the next step is to try using the API.
#Using the DropboxClient class - notice that i still need to use full dropbox.client.DropboxClient()
#https://www.dropbox.com/developers/core/docs/python#DropboxClient.account_info 
dbclient = dropbox.client.DropboxClient(access_token, locale="en-US", rest_client=None)

if user_id:
	userDetail = dbclient.account_info()
	print "---------------------------------"
	print "Log in complete."
	print "................................."
	print "Display name: " + userDetail['display_name']
	print "Email: " + userDetail['email']
	print "User Id: " + str(userDetail['uid'])
	print "................................."

	#working with files
	#uploading a file
	testfile = open('test.txt', 'rb')
	response = dbclient.put_file('/test.txt', testfile)
	print "uploaded file:", response['path']
	print "................................."

	#retrieving the content of a folder
	folder_metadata = dbclient.metadata('/')
	print "folder: ", folder_metadata['path']
	print "................................."

	#downloading a file
	testfile, metadata = dbclient.get_file_and_metadata('/test.txt')
	out = open('test.txt', 'wb')
	out.write(testfile.read())
	out.close()
	print "downloaded file: ", metadata['path']
	print "................................."
else:
	print "Sadly, something went wrong."



