from rest_framework import serializers
from .models import Movie
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomJWTSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["is_superuser"] = user.is_superuser
        return token


class MovieSerializer(serializers.Serializer):
    RATING_CHOICES = {
        ("G", "G"),
        ("PG", "PG"),
        ("PG-13", "PG-13"),
        ("R", "R"),
        ("NC-17", "NC-17"),
    }
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, default="", allow_blank=True)
    rating = serializers.ChoiceField(default="G", choices=RATING_CHOICES)
    synopsis = serializers.CharField(default="", required=False, allow_blank=True)
    added_by = serializers.CharField(source="user.email", read_only=True)

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
