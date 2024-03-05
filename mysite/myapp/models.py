"""
All Models
"""

from django.db import models
from django.core.validators import MinLengthValidator


class Book(models.Model):
    """
    Details of book
    """

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13, validators=[MinLengthValidator(13)])

    def __str__(self):
        """
        display name
        """
        return f"{self.title}"


class Car(models.Model):
    """
    Details of car
    """

    transmission_choices = [("Automatic", "Automatic"), ("Manual", "Manual")]

    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    transmission = models.CharField(
        choices=transmission_choices, max_length=10, default="Manual"
    )

    def __str__(self):
        """
        display name
        """
        return f"{self.make}"


class Song(models.Model):
    """
    Details of song
    """

    genre_choices = [
        ("Pop", "Pop"),
        ("Rock", "Rock"),
        ("Hip Hop", "Hip Hop"),
        ("Electronic", "Electronic"),
    ]
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=50)
    genre = models.CharField(max_length=10, choices=genre_choices)
    duration = models.FloatField()

    def __str__(self):
        """
        display name
        """
        return f"{self.title}"


class Movie(models.Model):
    """
    Details of movie
    """

    rating_choices = [
        ("G", "G"),
        ("H", "H"),
        ("I", "I"),
        ("J", "J"),
        ("K", "K"),
        ("L", "L"),
        ("M", "M"),
        ("N", "N"),
        ("O", "O"),
        ("P", "P"),
        ("Q", "Q"),
        ("R", "R"),
    ]

    title = models.CharField(max_length=100)
    director = models.CharField(max_length=50)
    release_year = models.IntegerField()
    rating = models.CharField(max_length=10, choices=rating_choices)

    def __str__(self):
        """
        display name
        """
        return f"{self.title}"


class JobPosting(models.Model):
    """
    Details of job
    """

    employment_choices = [
        ("Full-time", "Full-time"),
        ("Part-time", "Part-time"),
        ("Contract", "Contract"),
    ]

    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    employment_type = models.CharField(choices=employment_choices, max_length=20)

    def __str__(self):
        """
        display name
        """
        return f"{self.title}"


class Category(models.Model):
    """
    Details of category
    """

    name = models.CharField(max_length=50)

    def __str__(self):
        """
        display name
        """
        return f"{self.name}"


class Product(models.Model):
    """
    Details of product
    """

    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        """
        display name
        """
        return f"{self.name}"


class Project(models.Model):
    """
    Details of product
    """

    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        """
        display name
        """
        return f"{self.name}"


class Task(models.Model):
    """
    Details of task
    """

    name = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        """
        display name
        """
        return f"{self.name}"


class PostCategory(models.Model):
    """
    Details of category
    """

    name = models.CharField(max_length=50)

    def __str__(self):
        """
        display name
        """
        return f"{self.name}"


class Post(models.Model):
    """
    Details of post
    """

    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey(PostCategory, on_delete=models.CASCADE)

    def __str__(self):
        """
        display name
        """
        return f"{self.title}"


class Student(models.Model):
    """
    Details of student
    """

    name = models.CharField(max_length=100)

    def __str__(self):
        """
        display name
        """
        return f"{self.name}"


class Course(models.Model):
    """
    Details of course
    """

    name = models.CharField(max_length=100)

    def __str__(self):
        """
        display name
        """
        return f"{self.name}"


class Enrollment(models.Model):
    """
    Details of enrollment
    """

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.CharField(max_length=2)

    def __str__(self):
        """
        display name
        """
        return f"{self.grade}"
