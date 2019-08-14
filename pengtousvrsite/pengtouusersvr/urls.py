from django.conf.urls import url 

from user import views
from rest_framework import routers

router = routers.DefaultRouter()

app_name = 'pengtouusersvr'

urlpatterns =[
    url(r'get_user/$', views.get_user, name='get_user'),
    url(r'create_user/$', views.create_user, name='create_user'),
    url(r'update_user/$', views.update_user, name='update_user'),
        ]
