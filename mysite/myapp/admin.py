"""
Admin Panel View
"""

from django.contrib import admin
from .models import Book, Car, Song, Movie, JobPosting, Product, Task, Post, Enrollment

# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    to display Book class on admin panel
    """

    list_display = ["title", "author", "publication_date", "isbn"]


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    """
    to display Car class on admin panel
    """

    list_display = ["make", "model", "year", "transmission"]


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    """
    to display Song class on admin panel
    """

    list_display = ["title", "artist", "genre", "duration"]


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    """
    to display movie class on admin panel
    """

    list_display = ["title", "director", "release_year", "rating"]


@admin.register(JobPosting)
class JobPostingAdmin(admin.ModelAdmin):
    """
    to display jobposting class on admin panel
    """

    list_display = ["title", "company", "location", "employment_type"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    to display product class on admin panel
    """

    list_display = ["name", "description", "category"]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """
    to display task class on admin panel
    """

    list_display = ["name", "description", "project"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    to display post class on admin panel
    """

    list_display = ["title", "content", "category"]


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    """
    to display enrollment class on admin panel
    """

    list_display = ["student", "course", "grade"]
