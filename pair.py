from helper import load_config, get_variable
import yaml
from client import Client
configuration = load_config()
institution = get_variable(configuration, "institution")
connect_code = get_variable(configuration, "connect_code")

client = Client(school=institution)
access_token = client.authenticate(connect_code)
print ("This is your access token, put it in a safe location and in the config.yaml file! ACCESS_TOKEN: "+str(access_token["access_token"]))
