from django.urls import path

from .views import EstimatorView, LogView, EstimatorXMLView

urlpatterns = [
    path('', EstimatorView.as_view()),
    path('/json', EstimatorView.as_view()),
    path('/xml', EstimatorXMLView.as_view()),
    path('/logs', LogView.as_view())
]

