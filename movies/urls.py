from django.urls import path
from .views import MovieView, MovieDetailView
from movies_orders.views import MovieOrderView

urlpatterns = [
    path(
        "movies/",
        MovieView.as_view(),
        name="movie-create"
        ),
    path(
        "movies/<int:movie_id>/",
        MovieDetailView.as_view(),
        name="movie-detail"
        ),
    path(
        "movies/<int:movie_id>/orders/",
        MovieOrderView.as_view(),
        name="movie-order",
    ),
]
