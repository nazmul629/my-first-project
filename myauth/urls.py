from django.urls import path

from .views import *


urlpatterns = [
        path('login/',user_login, name = "user_login_url" ),
        path('logout/',user_logout, name = "user_logout_url"),
        path('singup/',user_signup, name ="signup_urls")
]