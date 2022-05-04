# BFDjango2022
Backend course
## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/Tairascii/BFDjango2022.git
$ cd papka
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd final
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/admin/`.

## Requirements

1. Maximum one page description of the project, mainfeatures 🟩 
2. Class diagram with all relations between entities 🟩 
3. Minimum 6 models (a.model inheritance, b.abstract model) 🟩 
4. Minimum 4 model Manager 🟩 
5. Minimum 6 relations between models (ForeignKey) 5/6 🟨
6. JWT Auth, Profile 🟩
7. Serializer (a. at least 2 from serializer.Serializer b. at least 2 serializer from serializer.ModelSerializer c. at least 4 Serializer inheritance d. at least 6 validations e. Nested serializer) 🟩 
8. Views (a. at least 2 FBV view b. at least 4 CBV APIView c. at least 6 ViewSet d. File Upload views) 🟩 
9. Django Signals - at least 4 usage 🟥
10. Logging module for each app 🟩 
11. Well structured Postman requests with all implementedmethods (a. separated by Folders b. using Environment variables (ex: token)) 🟩 
12. GitHub repo with well described Readme.md 🤞🏾
