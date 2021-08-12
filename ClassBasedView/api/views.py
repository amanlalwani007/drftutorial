from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.views import APIView
class StudentApi(APIView):
    def get(self,request,format=None):
        id =request.data.get('id')
        if id is not None :
            stu=Student.object.get(id=id )
            serializer=StudentSerializer(stu)
            return Response(serializer.data,status=status.HTTP_200_OK)
        stu=Student.objects.all()
        serializer= StudentSerializer(stu,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request,format=None):
        data= request.data
        serializer= StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'})
        return Response(serializer.errors)
    def put(self,request,format=None):
        id =request.data.get('id')
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializer(stu,data= request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data updated'})
    def delete(self,request,format=None):
        id =request.data.get('id')
        stu=Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})

