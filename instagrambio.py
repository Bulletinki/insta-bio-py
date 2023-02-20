from instagrapi import Client
import datetime

username = "USERNAME"
password = "PASSWORD"
email = "EMAIL"

cl = Client()
cl.login(username, password)

formatted_date = datetime.datetime.now().strftime("It is the %dst of %B, %Y. the time is %I:%M%p")

new_bio = formatted_date
print(new_bio)

cl.account_edit(email=email, phone_number="", full_name="", biography=new_bio, external_url="")
