from django.urls import path

from . import views

app_name = 'people'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('database/', views.database, name='database'),
    path('database/employee/', views.employee, name='employee'),
    path('database/user/', views.user, name='user'),
]