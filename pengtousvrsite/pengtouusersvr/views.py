from django.shortcuts import render, get_object_or_404
from django.utils import timezone
import json

from django.http import HttpResponse
from ../pengtoudaosvr/models import user, user_party
from django.core import serializers 
import requests 
import urllib.request
import urllib.parse

@api_view(['GET', 'POST'])
def get_user(request):
    if request.method == 'GET':
        users = user.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        user = user(uin=request.POST.get('uin'))
        serializer = UserSerializer(user)
        return Response(serializer.data)

@api_view(['Get', 'POST'])
def create_user(request):
    if request.method == 'POST':
        user = user(uin=request.POST.get('uin'),
                name=request.POST.get('name'),
                headurl=request.POST.get('headurl'),
                sex=request.POST.get('sex'))
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data)

@api_view(['Get', 'POST'])
def update_user(request):
    if request.method == 'POST':
        user = user.objects.get(uin=request.POST.get('uin'))
    if user:
        user.name = request.objects.get('name')
        user.headurl=request.objects.get('headurl')
        user.sex=request.objects.get('sex')
        user.update_time = timezone.localtime()

        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data)
    else:
        return JsonResponse({})

        

# Create your views here.
