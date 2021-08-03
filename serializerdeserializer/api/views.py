from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse

def student_detail(request,pk):
    stu =Student.objects.get(id =pk)
    # converting  queryset to python data
    serializer=StudentSerializer(stu)
    # serializer.data is the python is the native  python data
    json_data=JSONRenderer().render(serializer.data)
    #render is converting python native  datatype to json
    # return HttpResponse(json_data,content_type='application/json')
    #rather than writting content typr and application response we can directly write json  response`
    # return JsonResponse(serializer.data,safe=False) whwn there is python data and not renderred data
    return JsonResponse(serializer.data)



def student_list(request):
    stu =Student.objects.all()
    # converting  queryset to python data
    serializer=StudentSerializer(stu,many=True)
    # serializer.data is the python is the native  python data
    json_data=JSONRenderer().render(serializer.data)
    #render is converting python native  datatype to json
    return HttpResponse(json_data,content_type='application/json')
