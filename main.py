import datetime
from client import Client
import yaml

access_token = ""

def load_config():
    with open("config.yaml", "r") as configuration_file:
        config = yaml.safe_load(configuration_file)

    if config == None:
        raise ValueError("config.yaml is empty! Please fill in your credentials")

    return config

def get_variable(config, variable):
    if variable in config and not config[variable] == None:
        return config[variable]
    else:
        raise ValueError(f"{variable} not defined")

configuration = load_config()
institution = get_variable(configuration, "institution")

current_year = datetime.date.today().year
current_week = datetime.date.today().isocalendar()[1]

client = Client(school=institution)
usercode = client.get_user(token=access_token)["response"]["data"][0]["code"]
print(usercode)
print (client.get_liveschedule(token=access_token, week=str(current_year)+str(current_week), usercode=int(usercode)))