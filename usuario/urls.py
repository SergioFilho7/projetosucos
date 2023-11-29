from django.urls import path
from .views import *

urlpatterns=[
    path('usuario/index', index, name='index'),
    path('usuario/log_user', log_user, name='log_user'),
    path('usuario/cad_user', cad_user, name='cad_user'),
]