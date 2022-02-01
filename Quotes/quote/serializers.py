from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        #fields = ('id','last_login','is_superuser','last_name','is_staff','is_active','date_joined','first_name')
        exclude = ('password', )
