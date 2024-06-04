from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer, CustomTokenSerializer, LoginSerializer, ReportSerializer, CrimeCodeSerializer
from .models import Report, CrimeCode 
from .permissions import IsOwnerOrIsAdminOrReadOnly
from rest_framework.authentication import TokenAuthentication

from django.contrib.auth import authenticate

class SignUpView(APIView):
  def post(self, request):
    user_serializer = UserSerializer(data=request.data)
    user_serializer.is_valid(raise_exception=True)
    if user_serializer.is_valid():
      user = user_serializer.save()
      token, created = Token.objects.get_or_create(user=user)
      serializer = CustomTokenSerializer(data={'token': token.key, 'user': UserSerializer(user).data})
      serializer.is_valid()
      return Response(serializer.data, status=status.HTTP_201_CREATED)

class SignInView(APIView):
  permission_classes = [AllowAny]

  def post(self, request):
    print(request.data)
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      user = authenticate(username=serializer.data['username'], password=serializer.data['password'])
      token, created = Token.objects.get_or_create(user=user)
      serializer = CustomTokenSerializer(data={'token': token.key, 'user': UserSerializer(user).data})
      serializer.is_valid()
      return Response(serializer.data)

class ReportViewSet(viewsets.ModelViewSet):
  authentication_classes = [TokenAuthentication]
  permission_classes = [IsAuthenticated, IsOwnerOrIsAdminOrReadOnly]
  queryset = Report.objects.all()
  serializer_class = ReportSerializer

class CrimeCodeView(APIView):
  def get(self, request, format=None):
    queryset = CrimeCode.objects.all()
    serializer = CrimeCodeSerializer(queryset, many=True)
    return Response(serializer.data)