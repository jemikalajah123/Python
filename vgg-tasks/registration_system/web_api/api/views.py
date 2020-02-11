from django.shortcuts import render,redirect,get_list_or_404
from . models import Users,Projects,Actions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework import status
from . serializers import UsersSerializer,ProjectsSerializer,ActionsSerializer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,Http404
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser

class user_view(APIView):
    def post(self, request, format=None):

        if request.method == 'POST':
            serializer = UsersSerializer(data=request.data)
            data = {}
            if serializer.is_valid():
                user = serializer.save()
                data['response'] = "successfully registered a new user"
                data['username'] = user.username       
            else:
                data = serializer.errors
            return Response(data)


class projectList(APIView):
    def get(self, request):
        project1 = Projects.objects.all()
        serializer = ProjectsSerializer(project1, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        if request.method == 'POST':
            serializer = ProjectsSerializer(data=request.data)
            data = {}
            if serializer.is_valid():
                user_project = serializer.save()
                data['response'] = "successfully registered a new Project"
                data['name'] = user_project.name
            else:
                data = serializer.errors
            return Response(data)


class project_view(APIView):
    def get(self, request, id):

        try:
            project_user = Projects.objects.get(id=id)
        except project_user.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if  request.method == 'GET':
            serializer = ProjectsSerializer(project_user)
            return Response(serializer.data)


    def put(self, request, id):
        try:
            project_user = Projects.objects.get(id=id)
        except project_user.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if  request.method == 'PUT':
            serializer = ProjectsSerializer(project_user, data=request.data)
            data = {}
            if serializer.is_valid():
                serializer.save()
                data["success"] = "Update successful"
                return Response(data=data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            project_user = Projects.objects.get(id=id)
        except project_user.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if  request.method == 'DELETE':
            operation = project_user.delete()
            data = {}
            if operation:
                data["success"] = "delete successful"
            else:
                data["failure"] = "delete failed"
            return Response(data=data)

class action_view(APIView):
    def get(self, request):
        project1 = Actions.objects.all()
        serializer = ActionsSerializer(project1, many=True)
        return Response(serializer.data)

class action_id_view(APIView):   
    def get(self, request, id):

        try:
            project_user = Actions.objects.get(id=id)
        except project_user.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if  request.method == 'GET':
            serializer = ActionsSerializer(project_user)
            return Response(serializer.data)

class action_userview(APIView):
    def get(self, request, id):

        try:
            action_user = Actions.objects.get(project_id=id)
        except action_user.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if  request.method == 'GET':
            serializer = ActionsSerializer(action_user)
            return Response(serializer.data)


    def post(self, request, format=None):
        try:
            action_user = Actions.objects.get(id=id)
            project_user = Projects.objects.get(id=id)
        except action_user.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'POST':
            if action_user == project_user:
                serializer = ActionsSerializer(action_user, data=request.data)
                data = {}
            if serializer.is_valid():
                user_action = serializer.save()
                data['response'] = "successfully registered a new Project"
                data['project_id'] = user_action.project_id
            else:
                data = serializer.errors
            return Response(data)

class  action_Id_user(APIView): 
    def get(self, request, id, pk):

        try:
            action_user = Actions.objects.get(project_id=id)
            project_user = Actions.objects.get(id=pk)
        except action_user.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if  request.method == 'GET':
            if project_user == action_user:
                serializer = ActionsSerializer(project_user)
                return Response(serializer.data)

    def put(self, request, id, pk):
        
        try:

            action_user = Actions.objects.get( project_id=id)
            project_user = Actions.objects.get(id=pk)
        except action_user.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if  request.method == 'PUT':
            if project_user == action_user:
                serializer = ProjectsSerializer(project_user, data=request.data)
                data = {}
                if serializer.is_valid():
                    serializer.save()
                    data["success"] = "Update successful"
                    return Response(data=data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, pk):

        try:

            action_user = Actions.objects.get( project_id=id)
            project_user = Actions.objects.get(id=pk)
        except action_user.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if  request.method == 'DELETE':
            if project_user == action_user:
                operation = project_user.delete()
                data = {}
                if operation:
                    data["success"] = "delete successful"
                else:
                    data["failure"] = "delete failed"
                return Response(data=data)

