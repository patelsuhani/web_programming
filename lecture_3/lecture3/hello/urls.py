from django.urls import path

from . import views

urlpatterns = [
    # to create our first url pattern, we need to import the path function from the django.urls module
    # urlpatterns is a list of path() functions
    # first argument is empty string, which means no additional argument, meaning nothing at the end of the route.
    # second argument is what view should be rendered when this URL is visited
    # views represents views.py file in the hello app
    # index represents the index function in the views.py file
    # name makes it easy to refer to this URL elsewhere in Django, especially in templates 
    path("", views.index, name="index")
]