from django.http import HttpResponse
from rest_framework.views import APIView
from .models import Users
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework import status
from .serializers import TaskSerializer
import coreapi
from rest_framework.schemas import AutoSchema
class ApiListViewSchema(AutoSchema):
    def __init__(self):
        super(ApiListViewSchema, self).__init__()
    def get_manual_fields(self,path,method):
        extra_fields=[]
        if method.lower() in ['post','put']:
            extra_fields=[
                coreapi.Field('user_name',required=True),
                coreapi.Field('user_fname',required=True),
                coreapi.Field('user_age',required=True),
                coreapi.Field('user_address',required=True),
                coreapi.Field('user_country',required=True)
                
            ]
        manual_fields = super().get_manual_fields(path,method)
        return manual_fields + extra_fields    
class getpost(APIView):
    ApiListViewSchema()
    def get(self,request):
        user1 = Users.objects.all()
        serializer = TaskSerializer(user1 , many=True)
        return Response(serializer.data)
    def post(self,request):
        schema = ApiListViewSchema()
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
class delput(APIView):
    ApiListViewSchema()
    def delete(self,request,id):
        schema = ApiListViewSchema()
        user1 = Users.objects.get(id=id)
        user1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def put(self,request,id):
        user1 = Users.objects.get(id=id)
        serializer = TaskSerializer(user1 , data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)   
    def get(self,request,id):
        user1 = Users.objects.get(id=id)
        serializer = TaskSerializer(user1 , many=False)
        return Response(serializer.data)
