import dropbox

#Set up the App Secret - you get this from the developer page in your DB account:
#if this dosnt exist, you must create an app with appropriate permissions through the web portal
app_key = 'hi308thvvbnghlh'  
app_secret = '9la222bag3gwp6q'

#You'll need to provide your app key and secret to the new DropboxOAuth2FlowNoRedirect object.
#DropboxOAuth2FlowNoRedirect is a OAuth 2 authorization helper for apps that can't provide a 
#redirect URI (such as the command-line example apps).
flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)

#Authorize the app to use Dropbox - the return value is the URL we will print to the screen to have
#the user manually enter in thier browser to get this thing approved

# Have the user sign in and authorize this token
authorize_url = flow.start()
print '1. Go to: ' + authorize_url
print '2. Click "Allow" (you might have to log in first)'
print '3. Copy the authorization code.'
code = raw_input("Enter the authorization code here: ").strip()

#Once the user has delivered the authorization code to our app, 
#we can exchange that code for an access token via finish:
# This will fail if the user enters an invalid authorization code
access_token, user_id = flow.finish(code)

if user_id:
	print "User Id: " + str(user_id)
else:
	print "Sadly, something went wrong."



