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
choices={
    "1":2,
    "2":2,
    "3":3,
    "4":1,
    "5":2,
    "6":1,
    "7":3,
    "8":1,
    "9":1,
    "10":1,
    "11":2,
    "12":3,
    "13":1,
    "14":1,
    "15":2
}

@api_view(["POST"])
def sugg(request):
        
    user_interests = []
    for key, value in request.POST.items():
        user_interests.append(value)
    # for interest in request.data["interests"]:
    #     user_interests.append(interest)

    # return Response(user_interests)
    try:
        score=0
        for i in user_interests:
            if i in choices.keys():
                score+=choices[i]
                
        if score<5:
            suggestion=1
        elif score>=5 and score<10:
            suggestion=2
        elif score>=10 and score<15:
            suggestion=3    
        elif score>=15 and score<20:
            suggestion=4
        elif score>=20:
            suggestion=5

        suggestionJson = {
            "suggested_profession" : suggestion
        }
            
        return JsonResponse(suggestionJson)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)
    
