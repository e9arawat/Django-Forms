"""
URLS
"""

from django.urls import path
from .views import (
    HomeView,
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
    AddCategory,
    AddProject,
    AddPostCategory,
    AddStudent,
    AddCourse
)


urlpatterns = [
    path("", HomeView.as_view(), name="index"),
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
    path("add_category/", AddCategory.as_view(), name="add_category"),
    path("add_project/", AddProject.as_view(), name="add_project"),
    path("add_post_category/", AddPostCategory.as_view(), name="add_post_category"),
    path("add_student/", AddStudent.as_view(), name="add_student"),
    path("add_course/", AddCourse.as_view(), name="add_course"),
]
