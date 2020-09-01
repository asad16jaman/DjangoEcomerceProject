from django.urls import path
from . import views

app_name='Login_app'
urlpatterns=[
    path('singup/',views.sign_up,name='signup'),
    path('login/',views.mylogin,name='login'),
    path('logout/',views.logout_func,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('change_profile/',views.userchange,name='changeProfile'),
    path('password/',views.change_passwordform,name='change_pass'),
    path('add_pro_pic/',views.update_pro_pic,name='add_pic'),
    path('change_pro_pic/',views.change_pro_pic,name='change_pic')
]

