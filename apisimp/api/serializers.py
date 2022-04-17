from django.contrib.auth.models import User, Group
from django.db.models import fields
from rest_framework import serializers


# relationships are based on hyperlinks than pk
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


# Group serializer
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
