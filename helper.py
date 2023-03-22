import yaml
import pathlib
from gcsa.google_calendar import GoogleCalendar
from os.path import exists

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

def init_gcalendar():
    dir_path = pathlib.Path(__file__).parent.resolve()
    filename = "credentials.json"
    full_path = f"{dir_path}/{filename}"

    if not exists(full_path):
        raise ValueError(f"File: {full_path} doesn't exist!")
        
    return GoogleCalendar(credentials_path=full_path)