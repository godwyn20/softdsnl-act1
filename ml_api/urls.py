from django.urls import path
from .views import PredictIris

urlpatterns = [
    path('predict/', PredictIris.as_view(), name='predict-iris'),
]