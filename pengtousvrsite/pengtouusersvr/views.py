from django.shortcuts import render, get_object_or_404
import json

from django.http import HttpResponse
from ../pengtoudaosvr/models import user, user_party
from django.core import serializers 
import requests 
import urllib.request
import urllib.parse

def get_user(user_name):
    try:
        return user.objects.get(name=user_name)
    except user.DoesNotExist:
        return None


# Create your views here.
