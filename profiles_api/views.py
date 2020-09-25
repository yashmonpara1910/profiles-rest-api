from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

class HelloApiView(APIView):
    """Text API View"""
    serializer_class = serializers.HelloSerializer
    
    def get(self, request, format=None):
        """Retrun a list of API view features"""

        an_apiview = [
            'Uses HTTP methods as a function (get, post, patch, put, delete)',
            'Is similar to traditional Django view',
            'Gives the most control over your application',
            'Is mapped manually to the URL',
        ]

        return Response({'message' : 'Hello world', 'an_apiview': an_apiview})
    
    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        
        else:
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None):
        """Handle update of object"""
        return Response({'method': 'PUT'})
    
    def patch(self, request, pk=None):
        """Handle partial change of object"""
        return Response({'method': 'PATCH'})
    
    def delete(self, request, pk=None):
        """deleting an object """
        return Response({'method': 'DELETE'})