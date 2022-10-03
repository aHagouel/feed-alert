from twilio.rest import Client 
 
def start_client(account_sid = 'UR_SID', auth_token = 'UR_TOKEN'):
    return Client(account_sid, auth_token)


def send_alert_msg(client):
    message = client.messages.create( 
                                  from_='whatsapp:+14155238886',  
                                  body='Food is critically low, please re-fill.',      
                                  to='whatsapp:+16462067624' 
                              )
    print(message.sid)
