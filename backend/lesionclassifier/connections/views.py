
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

class Ping(View):   
    def get(self,request,*args,**kargs):
        return JsonResponse({"message":"pong"})

    def post(self,request,*args,**kargs):
        return JsonResponse({"message":"pong"})



