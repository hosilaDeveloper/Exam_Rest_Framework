from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Contact, About, TurPaket, Image

User = get_user_model()


class CustomRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        custom_user = User.objects.create_user(username=validated_data['username'], password=validated_data['password'])
        return custom_user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserLogoutSerializer(serializers.Serializer):
    username = serializers.CharField()


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'
        read_only_fields = ('custom_user',)


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class TurPaketSerializer(serializers.ModelSerializer):
    class Meta:
        model = TurPaket
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
