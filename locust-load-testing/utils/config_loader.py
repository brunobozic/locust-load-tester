import yaml

def load_config(file_name):
    with open(file_name, 'r') as file:
        return yaml.safe_load(file)

env_config = load_config('config/environments.yml')
load_test_config = load_config('config/load_config.yml')
endpoints = load_config('config/endpoints.yml')['endpoints']
credentials = load_config('config/credentials.yml')['credentials']
