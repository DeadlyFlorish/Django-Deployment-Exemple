from django.urls import path
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path('registre',views.registre,name='registre'),
    path('user_login',views.user_login,name='user_login')
]
