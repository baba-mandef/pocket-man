from root.settings import *

ALLOWED_HOSTS['https://pocket-man.herokuapp.com/']
DEBUG = False
TEMPLATES_DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY')
DATABASES['default'] = dj_database_url.config()