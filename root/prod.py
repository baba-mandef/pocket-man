from root.settings import *
import dj_database_url
ALLOWED_HOSTS = ['pocket-man.herokuapp.com']
DEBUG = False
TEMPLATES_DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY')
DATABASES['default'] = dj_database_url.config()
