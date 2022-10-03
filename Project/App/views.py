from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json

# Create your views here.


@api_view(['POST'])
def test(height_data):

    height = json.loads(height_data.body)["w"]
    weight = str(height*10)

    # res = JsonResponse("Ideal weight should be: "+weight+"key", safe=False)
    res = JsonResponse({"name": "Mukesh", "weight": weight+"kg"}, safe=False)
    return res







