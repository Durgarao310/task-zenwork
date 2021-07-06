from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from PyPDF2 import PdfFileReader
import io

@api_view(['GET'])
def crawl(request):
    if request.method == 'GET':
        url = 'https://www.treasury.gov/ofac/downloads/mbs/mbslist.pdf'
        response = requests.get(url)
        content = response.content.decode('latin-1')
        return Response(content)