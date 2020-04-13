from rest_framework import serializers
from .models import Log

class LogSerializer(serializers.ModelSerializer):
    final_log = serializers.SerializerMethodField()
    class Meta:
        model = Log
        # fields = ['method','path', 'status_code', 'response_ms']
        fields = ['final_log']
       


    def get_final_log(self, obj):
        return obj.final()

    def to_representation(self, data):
        # return {'method': data.method, 'path': data.path, 'status_code': data.status_code, 'response_ms': data.response_ms}
        return "{} \t {} \t{} \t{}ms \n".format(data.method, data.path, data.status_code, data.response_ms)

        