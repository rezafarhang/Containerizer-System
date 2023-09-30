from rest_framework import serializers
from .models import App, Container, RunningHistoryRecord


class AppSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)

    class Meta:
        model = App
        fields = ['name', 'image_address', 'envs', 'command', 'user']


class ContainerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Container
        fields = ['container_id', 'app', 'created_at', 'stopped_at']


class RunningHistoryRecordSerializer(serializers.ModelSerializer):
    
    container = serializers.CharField(read_only=True)
    status = serializers.CharField(read_only=True)
    envs = serializers.JSONField(read_only=True)

    class Meta:
        model = RunningHistoryRecord
        fields = ['container', 'status', 'envs', 'created_at']
    
