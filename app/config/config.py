import configparser

# Read configurations
config = configparser.ConfigParser()
config.read('configuration.ini')

wiki_url = config.get('URL', 'wiki_url')
api_key = config.get('API_KEY_AI', 'api_key')