from twilio.rest import Client
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import Outbound_sms
from twilio import twiml


def read_pairs():
    pairs = {0: 0}
    with open("pairs.txt", "r") as f:
        for line in f:
            little = line.split(',')[0]
            big = line.split(',')[1].rstrip('\n')
            pairs[little] = big
    return pairs


app = Flask(__name__)


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():

    pairs = read_pairs()

    t = 1

    number = request.form['From']
    msg = request.form['Body']
    resp = MessagingResponse()

    if t == 0:
        if msg == "Match Me!":
            resp.message("Here's how you find your new best friend! Take this quiz~ "
                          "https://goo.gl/forms/SVL03R49LqA38br62")
            with open("phone_numbers.txt", "a") as f:
                f.writelines(number + "\n")
        else:
            resp.message("Text us the magic word and we'll help you find your new best friend!")
    else:
        if msg in pairs:
            resp.message("{0} is your new best friend based on our matching algorithm. Put on your name tag and "
                         "see if you can find him/her in the crowd. Happy matching!".format(pairs[msg]))
        else:
            resp.message("ops, looks like we can't find you in our matching list. Was your text in the right format?"
                         "\n'FirstName LastName MM/DD/YYYY'\n")

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)




