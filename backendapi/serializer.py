from rest_framework import serializers
from .models import Log

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        # fields = ['method','path', 'status_code', 'response_ms']
        exclude = ['id']