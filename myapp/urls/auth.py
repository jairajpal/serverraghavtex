from django.urls import path
from ..views.auth import register, login, logout
from ..views.profile import get_profile, set_cookie

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('profile/', get_profile, name='profile'),
    path('set_cookie/', set_cookie, name='cookie'),
]
