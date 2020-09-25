from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Text API View"""
    def get(self, request, format=None):
        """Retrun a list of API view features"""

        an_apiview = [
            'Uses HTTP methods as a function (get, post, patch, put, delete)',
            'Is similar to traditional Django view',
            'Gives the most control over your application',
            'Is mapped manually to the URL',
        ]

        return Response({'message' : 'Hello world', 'an_apiview': an_apiview})
