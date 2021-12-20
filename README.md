# Registered-Users

## Instalation

- First clone this repository and Install Packages

```
git clone https://github.com/corteisjr/Registered-Users.git
pip install -r requirements.txt
```

- Setup Virtualenv Ubuntu  or Linux distro

```
python3 -m venv venv
source venv/bin/activate
```
- How To Setup on Windows

```
git clone https://github.com/corteisjr/Registered-Users.git
cd Registered-Users
python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt
```

- Migrate and start Server

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
