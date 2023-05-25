from django.urls import path
from .views import LoginView,RegisterView,PostsView
'''Cambiar int por string mirar como'''
urlpatterns = [
    path('login/',LoginView.as_view(),name='login_list'),
    path('login/<str:cedulaCiudadania>',LoginView.as_view(),name='login_process'),
    path('register/',RegisterView.as_view(),name='register_list'),
    path('register/<str:cedulaCiudadania_id>',RegisterView.as_view(),name='register_process'),
    path('posts/',PostsView.as_view(),name='posts_login'),
    path('posts/<int:id>',PostsView.as_view(),name='posts_process'),
]
