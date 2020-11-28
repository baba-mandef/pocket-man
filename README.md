# pocket-man

A little web-app to manage your personal finances

### Set the environment

##### install python and virtualenv
```shell script
sudo apt-get install python3
pip install virtualenv
```
##### create a new environment and install requirements
```shell script
virtualenv venv -p3
source venv/bin/activate
pip install -r requirements.txt
```

##### run the app
```shell script
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
Use postgresql, mysql or sqlite for database.