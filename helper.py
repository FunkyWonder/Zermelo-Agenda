import yaml

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