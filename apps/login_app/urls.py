from django.conf.urls import url
from . import views

urlpatterns = [
	#this is passing to views.py
    url(r'^$', views.index ),
    url(r'^register', views.register ),
    # url(r'^login', views.login ),
]