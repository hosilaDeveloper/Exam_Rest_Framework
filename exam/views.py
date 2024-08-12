from rest_framework.response import Response
from rest_framework import generics, permissions, status
from django.contrib.auth import get_user_model, authenticate
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .serializer import ContactSerializer, AboutSerializer, CustomRegisterSerializer, UserLogoutSerializer, \
    UserLoginSerializer
from .models import Contact, About

User = get_user_model()


class LoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            name = serializer.validated_data['name']
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password, name=name, email=email)
            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response({'username': user.username, 'token': token.key}, status=status.HTTP_200_OK)
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    def post(self, request):
        serializer = UserLogoutSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            name = serializer.validated_data['name']
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password, name=name, email=email)
            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response({'username': user.username, 'token': token.key}, status=status.HTTP_200_OK)
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CustomRegisterSerializer
    permission_classes = [permissions.AllowAny]


class ContactView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]


class AboutView(generics.ListCreateAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    permission_classes = [permissions.IsAuthenticated]
