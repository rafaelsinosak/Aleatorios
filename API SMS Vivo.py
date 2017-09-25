import twilio.rest
account_sid ="[seu id]"
auth_token ="[seu token"]


client = twilio.rest.TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
        body="".join(["rafaelsinosak\n" for i in range (10)]),
        to="+[seu numero]",
        from_="+16179257785"
    )

