from app.utils import get_env_name, get_config

env = get_config()

ENVIRONMENT = get_env_name()

APPLICATION_NAME = env['APPLICATION_NAME']
DEBUG = bool(env.get('DEBUG', False))
LOG_LEVEL = env['LOG_LEVEL']
TOKEN = env['TOKEN']
SQL_ALCHEMY_URI = env['SQL_ALCHEMY_URI']
