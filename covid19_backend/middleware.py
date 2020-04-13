import socket
import time
from django.utils.timezone import now
from backendapi.models import Log

class RequestLogMiddleware(object):
    def process_request(self, request):
        self.requested_at = now()


    def process_response(self, request, response):
        request_method = request.method
        request_path = request.get_full_path()
        response_status = response.status_code
        response_timedelta = now() - self.requested_at
        response_ms = int(response_timedelta.total_seconds() * 1000)
        newlog = Log()
        newlog.method = request_method
        newlog.path = request_path
        newlog.response_ms = response_ms
        newlog.status_code = response_status
        newlog.save()

        return response