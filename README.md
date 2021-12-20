# Registered-Users

-Home
[![Home.png](https://i.postimg.cc/Kz8dNVmw/Home.png)](https://postimg.cc/McgPZ9Mm)

-Registration Form
[![forms-Registration.png](https://i.postimg.cc/DwKfg2HN/forms-Registration.png)](https://postimg.cc/XpQ0N0VK)


## Acceptance criteria

-Criteria
  - Table with data of "registered" users
  - Button to open the user registration form
- User registration form
  - Form with the user information fields mentioned above
  - "Save" button to display the "Save successfully" dialog message.
  - "Cancel" button to return to user list

## Instalation

- First clone this repository and Install Packages

```
git clone https://github.com/corteisjr/Registered-Users.git
cd Registered-Users
pip install -r requirements.txt
```

- Setup Virtualenv Ubuntu  or Linux distro

```
python3 -m venv venv
source venv/bin/activate
```
- How To Setup on Windows

```
python -m venv venv
venv/Scripts/activate
```

- Migrate and start Server

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
