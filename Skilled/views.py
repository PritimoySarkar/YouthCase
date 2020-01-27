from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serailizers
from django.conf import settings
import json
# Create your views here.
choices={"Working with my hands":2,"Building and fixing things":2,"Working with computers":3,"Speaking or performing in front of others":1,"Working with machines and tools":2,"Singing, acting, dancing, or playing music":1,"Studying math or science":3,"Being creative (writing, art, etc.)":1,"Helping people solve problems":1,"Helping people feel better":1,"Selling things or ideas":2,"Working with numbers":3,"Being organized":1,"Following a set plan":1,"Taking industrial technology classes":2}








@api_view(["POST"])
def sugg(string):
    try:
        user_input=[]
        input1=input()
        while input1 !="":
            user_input.append(input1)
            input1=input()
        
        score=0
        for i in user_input:
            if i in choices.keys():
                score+=choices[i]
                
        if score<5:
            suggestion="Gardening"
        elif score>=5 and score<10:
            suggestion="Makeup"
        elif score>=10 and score<15:
            suggestion="Tailoring"    
        elif score>=15 and score<20:
            suggestion="Plumbing"
        elif score>=20:
            suggestion="Electrician"
            
        return JsonResponse(suggestion)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)
    