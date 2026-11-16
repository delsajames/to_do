from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework import authentication,permissions
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from accounts.permissions import IsOwner
from dailydo.serializers import ToDoSerializer
from dailydo.models import ToDo
from rest_framework.pagination import PageNumberPagination

# Create your views here.

class ToDoListCreateView(ListCreateAPIView):

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    serializer_class=ToDoSerializer

    def get_queryset(self):

        return ToDo.objects.filter(owner=self.request.user)


    def post(self,request):

        form_data=request.data

        serializer_instance=ToDoSerializer(data=form_data)

        if serializer_instance.is_valid():

            serializer_instance.save(owner=request.user)

            return Response(serializer_instance.data)
        
        else:

            return Response(serializer_instance.errors)

class ToDoRetrieveUpdateDeleteView(APIView):

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[IsOwner]

    def get(self,request,pk=None):

        qs=get_object_or_404(ToDo,id=pk)

        self.check_object_permissions(request,qs)

        serializer_instance=ToDoSerializer(qs)

        return Response(data=serializer_instance.data)

    def put(self,request,pk=None):

        form_data=request.data

        todo_object=get_object_or_404(ToDo,id=pk)

        self.check_object_permissions(request,todo_object)

        serializer_instance=ToDoSerializer(data=form_data,instance=todo_object)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)

    def delete(self,request,pk=None):

        todo_object=get_object_or_404(ToDo,id=pk)    

        self.check_object_permissions(request,todo_object)

        todo_object.delete()

        response_data={"message":"deleted"}

        return Response(response_data)



        

