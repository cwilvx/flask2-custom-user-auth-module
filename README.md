# flask2-custom-user-auth-module
A custom user auth module for a REST API built using Flask 2.0, Flask-Restful, MongoDb and Flask-JWT

### Local setup

```bash
# for ssh users
$ git clone git@github.com:geoffrey45/flask2-custom-user-auth-module.git

# for https
$ git clone https://github.com/geoffrey45/flask2-custom-user-auth-module.git

# for github desktop
$ gh repo clone geoffrey45/flask2-custom-user-auth-module

$ cd flask2-custom-user-auth-module

$ pip install -r requirements.txt

$ python manage.py
```

### Steps Part 1
1. Setting up the application factory
2. Write a simple auth view
3. Register a single user
4. Sign in a user
5. Refresh a JWT token
6. Get all users
7. Get single user by id

### Part 2
1. Update profile
2. Delete profile
3. Recover password via email
