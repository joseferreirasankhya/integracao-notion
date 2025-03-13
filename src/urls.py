from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from src import views

urlpatterns = [
    path('', views.home),
    path('hdi/send-data', views.send_data_to_csops)
]

urlpatterns = format_suffix_patterns(urlpatterns)
