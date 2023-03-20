import datetime
from client import Client

access_token = "ka63g5lff47e2k25aers8valc0"

instituion = "csghetstreek"

current_year = datetime.date.today().year
current_week = datetime.date.today().isocalendar()[1]

client = Client(school=instituion)
usercode = client.get_user(token=access_token)["response"]["data"][0]["code"]
print(usercode)
print (client.get_liveschedule(token=access_token, week=str(current_year)+str(current_week), usercode=int(usercode)))