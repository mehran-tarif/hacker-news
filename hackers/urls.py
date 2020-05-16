from django.urls import path
from . import views

app_name = 'hackers'

urlpatterns = [
    path('', views.LinkList.as_view(), name="home"),
]
