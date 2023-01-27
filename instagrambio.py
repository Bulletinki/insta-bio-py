from instagrapi import Client
import datetime

username = ""
password = ""

cl = Client()
cl.login(username, password)

formatted_date = datetime.datetime.now().strftime("It is the %dst of %B, %Y. the time is %I:%M%p")

new_bio = formatted_date
print(new_bio)

##cl.account_edit(email="davo.mailyan@gmail.com", phone_number="", full_name="", biography=new_bio, external_url="")