from rest_framework import generics, permissions, status, response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser


from .models import User
from .serializer import RegisterSerializer, LoginSerializer, LogoutSerializer, UserSerializer, PasswordSerializerWithToken
from .renderers import userRenderer

from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password


class RegisterAPIView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]
    renderer_classes = [userRenderer]
    def post(self, request, format=None):
        form_data = request.data
        serializer  = self.serializer_class(data=form_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return response.Response(serializer.data, status.HTTP_201_CREATED)
        
 

class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]
    def post(self, request, format=None):
        data = request.data
        email = data['email']
        password = data['password']

        user = authenticate(email=email, password=password)
        if not user:
            raise response.Response({'error': 'credentials are not valid'}, status=status.HTTP_401_UNAUTHORIZED)
        if not user.is_active:
            return response.Response({'error': 'credentials are not valid'}, status=status.HTTP_401_UNAUTHORIZED)
        # if not user.email_verified:
        #     raise response.Response({'error': 'credentials are not valid'}, status=status.HTTP_401_UNAUTHORIZED)
        if user:
            serializer = self.serializer_class(user)
            # 201 created, because it will create a refresh token and access token
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response({'error': 'credentials are not valid'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response({'success': 'successfully logged out'}, status=status.HTTP_204_NO_CONTENT)




@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updatePassword(request):
    user = request.user
    
    serializer = PasswordSerializerWithToken(user, many=False)

    data = request.data

    if data['password'] != '':
        user.password = make_password(data['password'])

    user.save()

    return response.Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUser(request, pk):
    user = User.objects.get(email=pk)

    data = request.data

    user.username = data['username']
    user.email = data['email']

    user.save()

    serializer = UserSerializer(user, many=False)

    return response.Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return response.Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return response.Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUserById(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return response.Response(serializer.data)





@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteUser(request, pk):
    userForDeletion = User.objects.get(id=pk)
    userForDeletion.delete()
    return response.Response('User was deleted')
