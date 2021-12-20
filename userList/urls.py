from django.urls import path
from . import views 

urlpatterns = [
    path('', views.listUser_view, name='listUser'),
    path("adduser", views.addUser_view, name='addUser'),
    path('users/<int:id>', views.userView, name='user')
]
