from rest_framework import serializers,status
from rest_framework.views import APIView
from .models import Person
from rest_framework.response import Response

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields= ["first_name","last_name","email"]

class PersonViewSet(APIView):
    
    def get(self,request,format=None):
        snippet = Person.objects.all()
        serializer = PersonSerializer(snippet,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)