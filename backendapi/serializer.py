from rest_framework import serializers
from .models import Log

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ['method','path', 'status_code', 'response_ms',]


    def to_representation(self, data):
        # return {'method': data.method, 'path': data.path, 'status_code': data.status_code, 'response_ms': data.response_ms}
        data['response_ms'] = str("{:02}".format(data['response_ms'])) + "ms"
        return "{} \t{} \t{} \t{} \n".format(data['method'], data['path'], data['status_code'], data['response_ms'])

        