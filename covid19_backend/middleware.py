import socket
import time
from backendapi.models import Log

class RequestLogMiddleware:
    def process_request(self, request):
        request.start_time = time.time()

    def process_response(self, request, response):
        # log_data = {
        #     'request_method': request.method,
        #     'request_path': request.get_full_path(),
        #     'http_status': response.status_code,
        #     'run_time': time.time() - request.start_time,
        # }
        new_data = Log()
        new_data.request_type = request.method
        new_data.request_path = request.get_full_path()
        new_data.http_status = response.status_code
        new_data.time_to_process = time.time() - request.start_time
        new_data.save()

        return response