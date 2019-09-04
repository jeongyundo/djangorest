from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from informationEvent import serializers
from informationEvent import models
from informationEvent import permissions

#apiview를 이용
class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview':an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        #받아온 데이터를 객체형태로 serialize를 시켜준다.
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            #f를 이용함으로써 {}를 사용할 수 있다. 그리고 이는 메세지를 제공한다
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method':'PUT'})
    #풋의 경우 모든 요소들을 업데이트 해야한다.

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Reponse({'method':'PATCH'})
    #패치의경우 특정 요소들만 업데이트 할 수 있다.

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})

#viewset을 이용
class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = serializers.HelloSerializer
    def list(self, request):
        """Return a hello message"""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update',
            'Automatically maps to URLs using Routhers',
            'Provides more functionality with less code' 
        ]

        return Response({'message':'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new Hello message"""
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({"message":message})
        else:
            return Response(
                serializer.error,
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method':"GET"})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method':"PUT"})

    def partial_update(self,request, pk=None):
        """Handle updating part of an object"""
        return Resopnse({"http_method":"PATCH"})

    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({"http_method":"DELETE"})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnProfile,)
