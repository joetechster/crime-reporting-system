# serializers.py
from rest_framework import serializers
from .models import CustomUser, Report, CrimeCode

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = '__all__'


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        # Field-level validation
        if not attrs.get('username'):
            raise serializers.ValidationError('Username is required.')
        if not attrs.get('password'):
            raise serializers.ValidationError('Password is required.')
        return attrs
      
class CustomTokenSerializer(serializers.Serializer):
    token = serializers.CharField(source='key')
    user = UserSerializer()
    

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'

class CrimeCodeSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = CrimeCode
        fields = '__all__'