import yaml
import pathlib
from gcsa.google_calendar import GoogleCalendar
from os.path import exists
from concurrent.futures import TimeoutError
from pebble import concurrent

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

@concurrent.process(timeout=60)
def create_process(path):
    return GoogleCalendar(credentials_path=path)

def init_gcalendar():
    dir_path = pathlib.Path(__file__).parent.resolve()
    filename = "credentials.json"
    full_path = f"{dir_path}/{filename}"

    if not exists(full_path):
        raise ValueError(f"File: {full_path} doesn't exist!")

    try:
        process = create_process(full_path)
        gc = process.result()
    except TimeoutError:
        print("User hasn't authenticated in 60 seconds")

    return gc

print(init_gcalendar())