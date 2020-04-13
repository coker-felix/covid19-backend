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
from covid19_backend.mixin import RequestLogViewMixin 
import json

from .models import Log
from .serializer import LogSerializer
from .PlainTextParser import PlainTextParser
from .PlainTextRenderer import PlainTextRenderer


# Create your views here.
class EstimatorView(RequestLogViewMixin, APIView):
	renderer_classes = (JSONRenderer, BrowsableAPIRenderer)
	parser_classes = (JSONParser,)
	def post(self, request):
		post_data = request.data
		output_data = estimator(post_data)
		return Response(output_data)


	def get(self, request):
		return Response()	


class EstimatorXMLView(RequestLogViewMixin, APIView):
	renderer_classes = (XMLRenderer,)
	parser_classes = (JSONParser,)
	def post(self, request):
		post_data = request.data
		output_data = estimator(post_data)	
		return Response(output_data)	

	def get(self, request):
		return Response()	        



class LogView(RequestLogViewMixin, ListAPIView):
	renderer_classes = (PlainTextRenderer,)
	# parser_classes = (PlainTextParser,)

	def get(self, request):
		logs = Log.objects.all()
		serializer = LogSerializer(logs, many=True)
		data = serializer.data
		return Response(data)	

	def post(self, request):
		logs = Log.objects.all()
		serializer = LogSerializer(logs, many=True)
		data = serializer.data
		return Response(data)

