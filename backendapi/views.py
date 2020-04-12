from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer, StaticHTMLRenderer, TemplateHTMLRenderer
from rest_framework_xml.renderers import XMLRenderer
from rest_framework_xml.parsers import XMLParser
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .Impact import computeForImpact
from .Severe import computeForSevereImpact
from .estimator import estimator
from .models import Log
from .serializer import LogSerializer
from covid19_backend.mixin import RequestLogViewMixin


# Create your views here.
class EstimatorView(RequestLogViewMixin, APIView):
	renderer_classes = (JSONRenderer, BrowsableAPIRenderer)
	def post(self, request, format=None):
		post_data = request.data
		output_data = estimator(post_data)
		return Response(output_data)


	def get(self, request, format=None):
		return Response()	


class EstimatorXMLView(RequestLogViewMixin, APIView):
	renderer_classes = (XMLRenderer,)
	def post(self, request, format='xml'):
		if request.accepted_media_type == 'application/xml':
			post_data = request.data
			output_data = estimator(post_data)	
			return Response(output_data)

	def get(self, request):
		return Response()	        



class LogView(APIView):
	# renderer_classes = (StaticHTMLRenderer,)
	# renderer_classes = (TemplateHTMLRenderer,)

	def get(self, request):
		logs = Log.objects.all()	
		serializer = LogSerializer(logs, many=True)	
		return Response(serializer.data)	



