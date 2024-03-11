from rest_framework.views import Response, Request, status, APIView
from .serializers import MovieOrderSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from movies.models import Movie
from django.shortcuts import get_object_or_404


class MovieOrderView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request: Request, movie_id) -> Response:
        movie = get_object_or_404(Movie.objects.all(), pk=movie_id)
        serializer = MovieOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user, movie=movie)
        return Response(serializer.data, status.HTTP_201_CREATED)
