from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.parsers import JSONParser
from rest_framework_xml.renderers import XMLRenderer
from rest_framework_xml.parsers import XMLParser
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .Impact import computeForImpact
from .Severe import computeForSevereImpact
from .estimator import estimator
from rest_framework_tracking.mixins import LoggingMixin
from rest_framework_tracking.base_models import BaseAPIRequestLog
from rest_framework_tracking.models import APIRequestLog
from covid19_backend.mixin import RequestLogViewMixin 
import json

from .models import Log
from .serializer import LogSerializer
from .PlainTextParser import PlainTextParser
from .PlainTextRenderer import PlainTextRenderer



from django.http import HttpResponse
# Create your views here.
class EstimatorView(LoggingMixin, APIView):
	renderer_classes = (JSONRenderer, BrowsableAPIRenderer)
	parser_classes = (JSONParser,)
	def post(self, request):
		post_data = request.data
		output_data = estimator(post_data)
		return Response(output_data)


	def get(self, request):
		return Response()	


class EstimatorXMLView(LoggingMixin,APIView):
	renderer_classes = (XMLRenderer,)
	parser_classes = (JSONParser,)
	def post(self, request):
		post_data = request.data
		output_data = estimator(post_data)	
		return Response(output_data)	

	def get(self, request):
		return Response()	        



class LogView(LoggingMixin, ListAPIView):
	renderer_classes = (PlainTextRenderer,)
	parser_classes = (PlainTextParser,)
	http_method_names = ['get']

	def get(self, request):
		xlogs = APIRequestLog.objects.values('method','path', 'status_code', 'response_ms',)
		serializer = LogSerializer(xlogs, many=True)
		data = serializer.data
		return Response(data)
		# return HttpResponse(data, content_type='text/plain; charset=utf-8')	

