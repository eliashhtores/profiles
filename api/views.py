from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.views import APIView
from .models import UserProfile, ProfileFeedItem
from .permissions import UpdateOwnProfile
from .serializers import HelloApiSerializer, UserProfileSerializer, ProfileFeedItemSerializer


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = HelloApiSerializer

    def get(self, request):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Creates a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello, {name}!'
            return Response({'message': message})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handles updating an entire object"""

        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handles updating part of an object"""

        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Deletes an object"""

        return Response({'method': 'DELETE'})


class HelloApiViewSet(ViewSet):
    """Test API ViewSet"""
    serializer_class = HelloApiSerializer

    def list(self, request):
        """Returns a hello message"""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update and destroy)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Creates a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello, {name}!'
            return Response({'message': message})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handles getting an object by its ID"""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handles updating an object"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handles updating part of an object"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handles removing an object"""

        return Response({'http_method': 'DELETE'})


class UserProfileApiViewSet(ModelViewSet):
    """Handles creating and updating profiles"""
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (UpdateOwnProfile, )
    filter_backends = (SearchFilter, )
    search_fields = ('name', 'email', )


class UserLoginApiView(ObtainAuthToken):
    """Handles creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ProfileFeedItemViewSet(ModelViewSet):
    """Handles creating, reading and updating profile feed items"""
    serializer_class = ProfileFeedItemSerializer
    queryset = ProfileFeedItem.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)
