from django.urls import path
from . import views
from account import views as account_views

app_name = 'hackers'

urlpatterns = [
    path('', views.LinkList.as_view(), name="home"),

    path('links', account_views.LinkList.as_view(), name="links"),
    path('delete/<int:pk>', account_views.LinkDelete.as_view(), name="delete"),
    path('create', account_views.LinkCreate.as_view(), name="create"),
    path('login', account_views.Login.as_view(), name="login"),
    path('register', account_views.Register.as_view(), name="register"),
    path('logout', account_views.Logout.as_view(), name="logout"),
]
