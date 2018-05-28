from django.shortcuts import render, Http404, HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from . serializers import *
import json
import datetime
from django.views.decorators.csrf import csrf_exempt


class exam1(APIView):

   def get(self, request):
    
      allpost = Exam1.objects.all()
      serializer = postSerializer1(allpost, many=True)
      return Response(serializer.data)

   def post(self):
      pass




class exam2(APIView):

   def get(self, request):
    
      allpost = Exam2.objects.all()
      serializer = postSerializer2(allpost, many=True)
      return Response(serializer.data)

   def post(self):
      pass


class exam3(APIView):

   def get(self, request):
    
      allpost = Exam3.objects.all()
      serializer = postSerializer3(allpost, many=True)
      return Response(serializer.data)

   def post(self):
      pass


class exam4(APIView):

   def get(self, request):
    
      allpost = Exam4.objects.all()
      serializer = postSerializer4(allpost, many=True)
      return Response(serializer.data)

   def post(self):
      pass

class exam5(APIView):

   def get(self, request):
    
      allpost = Exam5.objects.all()
      serializer = postSerializer5(allpost, many=True)
      return Response(serializer.data)

   def post(self):
      pass

class general_science(APIView):

   def get(self, request):
    
      allpost = General_science.objects.all()
      serializer = postSerializer6(allpost, many=True)
      return Response(serializer.data)

   def post(self):
      pass

class current_affairs(APIView):

   def get(self, request):
    
      allpost = Current_affairs.objects.all()
      serializer = postSerializer7(allpost, many=True)
      return Response(serializer.data)

   def post(self):
      pass


class english(APIView):

   def get(self, request):
    
      allpost = English.objects.all()
      serializer = postSerializer8(allpost, many=True)
      return Response(serializer.data)

   def post(self):
      pass



