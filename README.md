# Registered-Users

- Home
[![Home.png](https://i.postimg.cc/0QdstS12/Home.png)](https://postimg.cc/tZTwJYgL)

- Registration Form
[![forms-Registration.png](https://i.postimg.cc/gJd960L9/forms-Registration.png)](https://postimg.cc/Z9fsG4Lj)

- Table with data of "registered" users
[![Data.png](https://i.postimg.cc/KjzHn3ZW/Data.png)](https://postimg.cc/YG5R79LN)

## Acceptance criteria

- Criteria
  - Table with data of "registered" users
  - Button to open the user registration form
- User registration form
  - Form with the user information fields mentioned above
  - "Save" button to display the "Save successfully" dialog message.
  - "Cancel" button to return to user list

## Instalation

- First clone this repository and Install Packages

```terminal
git clone https://github.com/corteisjr/Registered-Users.git
cd Registered-Users
pip install -r requirements.txt
```

- Setup Virtualenv Ubuntu  or Linux distro

```terminal
python3 -m venv venv
source venv/bin/activate
```
- How To Setup on Windows

```terminal
python -m venv venv
venv/Scripts/activate
```

- Migrate and start Server

```terminal
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
