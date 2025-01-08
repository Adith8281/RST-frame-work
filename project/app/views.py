from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from .models import *
from .serializers import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

# def fun1(request):
#     if request.method=='GET':
#         data=student.objects.all()
#         s=studserializer(data,many=True)
#         return JsonResponse(s.data,safe=False)
    
    
# @csrf_exempt
# def fun1(request):
#     if request.method=='GET':
#         data=student.objects.all()
#         s=studmodelSerializer(data,many=True)
#         return JsonResponse(s.data,safe=False)
#     elif request.method=='POST':
#         d=JSONParser().parse(request)
#         s=studmodelSerializer(data=d)
#         print(s)
#         if s.is_valid():
#             s.save()
#             return JsonResponse(s.data,safe=False)
#         else:
#             return JsonResponse(s.errors)

# @csrf_exempt
# def fun1 (request,pk):
#     try:
#         demo=student.objects.get(pk=pk)
#         print('hello')
#     except:
#         return HttpResponse("invalid")
#     if request.method=='GET':
#         s=studmodelSerializer(demo)
#         return JsonResponse(s.data)
#     elif request.method=='PUT':
#         d=JSONParser().parse(request)
#         s=studmodelSerializer(demo,data=d)
#         if s.is_valid():
#             s.save()
#             return JsonResponse(s.data)
#         else:
#             return JsonResponse(s.errors)
#     elif request.method=='DELETE':
#             demo.delete()
#             return HttpResponse("Deleted")



# @api_view(['GET','POST'])
# def fun1(req):
#     if req.method == 'GET':
#         d=student.objects.all()
#         s=studmodelSerializer(d, many=True)
#         return Response(s.data)
#     elif req.method =='POST':
#         s=studmodelSerializer(data=req.data)
#         if s.is_valid():
#             s.save()
#             return JsonResponse(s.data,status=status.HTTP_201_CREATED)
#         else:
#             return JsonResponse(s.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def fun1(req,pk):
    try:
        demo=student.objects.get(pk=pk)
    except student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if req.method=='GET':
        s=studmodelSerializer(demo)
        return Response(s.data)
    elif req.method=='PUT':
        s=studmodelSerializer(demo,data=req.data)
        if s.is_valid():
            s.save()
            return Response(s.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    elif req.method=='DELETE':
        demo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        