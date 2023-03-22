import datetime
from client import Client
import yaml
from helper import load_config, get_variable

configuration = load_config()
institution = get_variable(configuration, "institution")
access_token = get_variable(configuration, "access_token")

current_year = datetime.date.today().year
current_week = datetime.date.today().isocalendar()[1]

client = Client(school=institution)
usercode = client.get_user(token=access_token)["response"]["data"][0]["code"]

print (f"Hi {usercode}, here's your current schedule:")
print (client.get_liveschedule(token=access_token, week=str(current_year)+str(current_week), usercode=int(usercode)))