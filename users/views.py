from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from django.http import Http404



class Register_user(APIView):
    
    def post(self,request,format=None):
        serializer=UserRegister(data=request.data)
        data={}
        if serializer.is_valid():
            account=serializer.save()
            data['response']='registered'
            data['username']=account.username
            data['email']=account.email
            token,create=Token.objects.get_or_create(user=account)
            data['token']=token.key
        else:
            data=serializer.errors
        return Response(data)


class UserPermission(APIView):
    permission_classes =(IsAuthenticated,)
    
    def get(self,request):
        content={'userid':str(request.user.id),'user':str(request.user),'user-email':str(request.user.email)}
        return Response(content)

class UserDetails(APIView):

    def get_object(self,pk):
        try:
            return User.objects.get(pk=pk)
        except:
            raise Http404
        
    def get(self,request,pk,format=None):
        userData=self.get_object(pk)
        serializer=UserDetailsSerializer(userData)
        return Response(serializer.data)

    def put(self,request,pk,format=None):
        userData=self.get_object(pk)
        serializer=UserDetailsSerializer(userData,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'message':'error','error':serializer.errors})

    def delete(self,request,pk,format=None):
        userData=self.get_object(pk)
        userData.delete()
        return Response({'message':"user deleted"})
