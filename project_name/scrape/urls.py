from django.urls import path
from .views import sca

urlpatterns = [
    path('scrape',sca),
]