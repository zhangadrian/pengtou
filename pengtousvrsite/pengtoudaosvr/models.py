from django.db import models
from datetime import datetime
from django.utils import timezone

class user(models.Model):
    uin = models.IntegerField(default=0)
    name = models.CharField(max_length=255)
    headurl = models.TextField()
    level = models.IntegerField(default=0)
    point = models.FloatField()
    join_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    hobby = models.CharField(max_length=255)
    sex = models.CharField(max_length=10)

    openid = models.CharField(max_length=100, blank=True)
    session_id = models.CharField(max_length=100, blank=True)
    code = models.CharField(max_length=100, blank=True)

    def __str_(self):
        return self.openid
    

class party(models.Model):
    party_id = models.AutoField(primary_key=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    finish_time = models.DateTimeField(default=timezone.now)
    user_list = models.TextField()
    poi_id = models.IntegerField(default=0)
    pro_num = models.IntegerField(default=0)
    con_num = models.IntegerField(default=0)

    def __str__(self):
        return party_id
    

class user_party(models.Model):
    uin = models.IntegerField(default=0)
    party_id = models.IntegerField(default=0)
    
    def __str__(self):
        return str(uin) + '_' + str(party_id)

class poi(models.Model):
    poi_id = models.IntegerField(default=0)
    addr = models.TextField()
    img_list = models.TextField()
    ugc = models.TextField()
    poi_type = models.CharField(max_length=100)
    score = models.FloatField()
    price = models.FloatField()
    name = models.CharField(max_length=255)
    special = models.TextField()

    def __str__(self):
        return poi_id

