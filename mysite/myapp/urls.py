"""
URLS
"""

from django.urls import path
from .views import (
    AddBook,
    AddCar,
    AddSong,
    SuccessView,
    AddMovie,
    AddJob,
    AddProduct,
    AddTask,
    AddPost,
    AddEnrollment,
)


urlpatterns = [
    path("success/", SuccessView.as_view(), name="success"),
    path("add_book/", AddBook.as_view(), name="add_book"),
    path("add_car/", AddCar.as_view(), name="add_car"),
    path("add_song/", AddSong.as_view(), name="add_song"),
    path("add_movie/", AddMovie.as_view(), name="add_movie"),
    path("add_job/", AddJob.as_view(), name="add_job"),
    path("add_product/", AddProduct.as_view(), name="add_product"),
    path("add_task/", AddTask.as_view(), name="add_task"),
    path("add_post/", AddPost.as_view(), name="add_post"),
    path("add_enrollment/", AddEnrollment.as_view(), name="add_enrollment"),
]
