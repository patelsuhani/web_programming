# Lecture 3

## Overview

Django - a Python web framework which allows programmers to write Python code that is able to dynamically generate HTML and CSS, ultimately allowing users to build a dynamic web application.

### HTTP 

* Hyper Text Transfer Protocol - protocol for how messages are going to be sent back and forth on the internet. 

* A user requests services (or gets pages) from the server using request methods. For example, in the following code snippet, I'm trying to get a slash page, just denoting the root of a website, usually the default page for the website.
```
GET / HTTP/1.1
Host: www.example.com
...
```

* HTTP/1.1 is the version of HTTP used.

* HOST is what URL you're trying to access the webpage for.

* A server processes the request and generates a response like the following:

```
HTTP/1.1 200 OK
Content-Type: text/html
...
```

* 200 is a response code that just means OK.
* The second line means that the format of the data that is coming back in this response is HTML data that the user's web browser should render as HTML.

* HTTP Status Codes
![table of some common HTTP Status Codes](./http_status_codes.jpeg)

* To create a Django project if you installed python from Windows Store, type in your terminal:
    - `python -m django startproject <project_name>`
    - django will automatically create some starter files for you.

* Django creates manage.py file which you can use to be able to execute commands on your Django project.

* settings.py contains important configuration settings for your Django application.

* urls.py is a table of contents of all URLs on your web application that one can ultimately visit.

* To run this project, type in terminal:
    - `python manage.py runserver`
    - runserver is a command
    - Where is your web application currently running? This statement provides the information: `Starting development server at http://127.0.0.1:8000/`
    - 127.0.0.1 is an IP address, an address on the internet that just refers to your local computer in this case.
    - 8000 is a port number. It refers to what type of service is being run.

* Next, you need to create a Django app as follows:
    - Type `python manage.py startapp <app_name>` in the terminal.
    - One Django project can have multiple Django apps.

* views.py is the file that lets you describe what it is that the user sees when they visit a particular route for example, where you can decide what gets rendered to the user.

* Next, add your app to the INSTALLED APPS LIST in settings.py. For example:
```
INSTALLED_APPS = [
    # adds your app called hello to a list which contains other predefined and pre-installed apps
    'hello',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

* To create a view in Django, you have to define a function in views.py

* Each app will have its own urls.py file so that if each app is doing something independent, we can have each of those individual apps have its own urls.py to control what URLs are available for that particular app.