from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(
        max_length=50,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="username already taken."
            )
        ],
    )
    email = serializers.EmailField(
        max_length=127,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="email already registered."
            )
        ],
    )
    birthdate = serializers.DateField(required=False, allow_null=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    is_employee = serializers.BooleanField(default=False)
    is_superuser = serializers.BooleanField(default=False, read_only=True)
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        if validated_data["is_employee"]:
            user = get_user_model().objects.create_superuser(**validated_data)
        else:
            user = get_user_model().objects.create_user(**validated_data)
        return user

    def update(self, instance: User, validated_data: dict):
        instance.username = validated_data.get("username", instance.username)
        instance.email = validated_data.get("email", instance.email)
        instance.birthdate = validated_data.get("birthdate", instance.birthdate)
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.is_employee = validated_data.get("is_employee", instance.is_employee)
        password = validated_data.get("password")
        if password:
            instance.set_password(password)

        instance.save()
        return instance
