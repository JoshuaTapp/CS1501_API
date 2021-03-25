import os
from twilio.rest import Client
import giphy_client


# GIPHY API
giphy_instance = giphy_client.DefaultApi()
api_key = '############' # GIPHY API KEY

random_url = giphy_instance.gifs_random_get(api_key).data.fixed_height_downsampled_url

# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = '#############' # twilio account ID
auth_token = '##############' # twilio secret key 
client = Client(account_sid, auth_token)


message = client.messages \
                .create(
                     from_='+###########', # twilio assigned number
                     media_url=[random_url],
                     to='+############'     # recipient's number
                 )

print(message.sid)
