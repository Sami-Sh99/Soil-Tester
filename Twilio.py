
###################################
#Send a msg to Sami's Phone Number#
###################################

from twilio.rest import Client

def send(text,account_sid,auth_token):


	client = Client(account_sid, auth_token)

	message = client.messages.create(
	    to="+96176928149", 
	    from_="+12563735535",
	    body=text)

	return(message.sid)