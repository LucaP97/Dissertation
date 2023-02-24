from django.urls import path
from . import views
# from tss import views as v

app_name = 'members'

urlpatterns = [
    path("login_user/", views.login_user, name="login"),
    path("register_user", views.register_user, name="register_user"),
    path("select_team", views.select_team, name="select_team"),
]