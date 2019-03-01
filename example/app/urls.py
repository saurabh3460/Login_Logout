from django.urls import path
from .views import *

urlpatterns = [
    path('', signup, name='signup'),
    path('signup/', signup, name='signup'),
    path('profile/', profile, name='profile'),
    path('logout/', Logout, name='logout'),
    path('login/', login, name='login'),

]