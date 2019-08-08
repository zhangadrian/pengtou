from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('api/getuserinfo', views.get_user_info, name='getUserInfo'),
        path('api/uploadcreateparty', views.upload_create_party, name='uploadCreateParty'),
]


