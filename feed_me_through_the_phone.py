from twilio.rest import Client 
 
def start_client(account_sid = 'your_sid', auth_token = 'your_auth_token'):
    return Client(account_sid, auth_token)


def send_alert_msg(client,fullness,time):
    
    msg = 'Detected critical feed level! \n Container is ' + fullness +'% full. \n Do you want Maui to be hungry?!'
    message = client.messages.create( 
                                  from_='whatsapp:+14155238886',  
                                  body=msg,
                                  to='whatsapp:+16462067624' 
                              )
    print(message.sid)
