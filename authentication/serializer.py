import uuid
from rest_framework import serializers
from .models import User

from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode


from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework.exceptions import AuthenticationFailed


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=170, min_length=8, write_only=True)
    class Meta:
        model = User
        fields = [
            'username', 'email', 'password'
        ]
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    

class UpdateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=170, min_length=8, write_only=True, required=False)
    password2 = serializers.CharField(max_length=170, min_length=8, write_only=True, required=False)    
    old_password = serializers.CharField(write_only=True, required=True)

    
    class Meta:
        model = User
        fields = [
            'username', 'email', 'password'
        ]

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):
        instance.set_password(validated_data['username'])
        instance.set_password(validated_data['email'])

        instance.set_password(validated_data['password'])
        instance.save()

        return instance


class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=1000)

    class Meta:
        model = User
        fields = [
            'token'
        ]


    
class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=170, min_length=8, write_only=True)
    class Meta:
        model = User
        fields = ['email', 'password', 'tokens']

        read_only_fields = ['tokens']

    
     

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_message = {
        'bad_token': ('Token is expired or invalid')
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token ')


class UserSerializer(serializers.ModelSerializer):
    _id = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', '_id', 'username', 'email']
        read_only_fields=['id','_id']


    def get__id(self, obj):
        return obj.id


    def get_name(self, obj):
        return obj.email

class PasswordSerializerWithToken(UserSerializer):
    password = serializers.CharField(max_length=170, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['id', '_id', 'username', 'email', 'tokens', 'password']
        read_only_fields=['id', '_id', 'username', 'email', 'tokens']

