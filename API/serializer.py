from django.db.models.base import Model
from rest_framework import serializers
from API.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model= Task
        fields= ['id','title','time']