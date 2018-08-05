
from twilio.rest import Client
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

def Outbound_sms():
    phone_numbers = []
    with open("phone_numbers.txt", "r") as f:
        phone_numbers.extend(f.readlines())
    print(phone_numbers)
    # Your Account SID from twilio.com/console
    account_sid = "AC033e67c3f6f5851a6e833a3736ff5ca8"
    # Your Auth Token from twilio.com/console
    auth_token = "ba7353c216d9929da568e90b35e20213"

    client = Client(account_sid, auth_token)
    for phone_number in phone_numbers:
        message = client.messages.create(
            to=phone_number,
            from_="+14845145299",
            body="The Matches are in! Text us your name and birthday in the format of"
                 "\n'FirstName LastName MM/DD/YYYY'\n "
                 "to find out who you get paired with!")
    print(message.sid)


if __name__ == "__main__":
    Outbound_sms()
