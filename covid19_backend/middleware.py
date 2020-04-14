import socket
import time
from django.utils.timezone import now
from backendapi.models import Log

class RequestLogMiddleware(object):
    def process_request(self, request):
        global started
        started = time.time()


    def process_response(self, request, response):
        request_method = request.method
        request_path = request.get_full_path()
        response_status = response.status_code
        total = time.time() - started
        response_ms = int(total * 1000)
        response_ms = max(response_ms, 0)
        newlog = Log()
        newlog.method = request_method
        newlog.path = request_path
        newlog.response_ms = response_ms
        newlog.status_code = response_status
        newlog.save()

        return response

        