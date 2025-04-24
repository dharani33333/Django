from django.contrib import admin
from django.urls import path
# from .views import homepage
from .views import html
urlpatterns = [
    # path("home",homepage),
    path("my_html",html)
]