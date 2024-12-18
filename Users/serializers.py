from django.contrib.auth.models import User
from .models import UserProfile
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.hashers import make_password

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True},
            'first_name': {'required': True}
        }
        
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        user = super().create(validated_data)
        profile = UserProfile.objects.create(user=user)
        profile.save()
        return user
    
    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super().update(instance, validated_data)
    
    def partial_update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super().partial_update(instance, validated_data)
    
    
class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'