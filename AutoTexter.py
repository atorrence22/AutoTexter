from twilio.rest import Client


account_sid = ''
auth_token = ''

client = Client(account_sid, auth_token)

NUMBERS = {

}

for name, number in NUMBERS.items():
    message = client.messages.create(
        to=number,
        from_='OUR_NUMBER',
        body="whatever the fuck we want"
)
