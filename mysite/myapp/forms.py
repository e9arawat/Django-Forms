"""
All forms
"""

from django import forms
from .models import Book, Car, Song, Movie, JobPosting, Product, Task, Post, Enrollment, Category, Project, PostCategory, Student, Course


class BookForm(forms.ModelForm):
    """
    form for adding a new book details
    """

    class Meta:
        """
        Meta calss
        """

        model = Book
        fields = "__all__"

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.TextInput(attrs={"class": "form-control"}),
            "publication_date": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "isbn": forms.TextInput(attrs={"class": "form-control"}),
        }


class CarForm(forms.ModelForm):
    """
    form for adding a new car details
    """

    class Meta:
        """
        Meta class
        """

        model = Car
        fields = "__all__"

        widgets = {
            "make": forms.TextInput(attrs={"class": "form-control"}),
            "model": forms.TextInput(attrs={"class": "form-control"}),
            "year": forms.NumberInput(attrs={"class": "form-control"}),
            "transmission": forms.RadioSelect(),
        }


class SongForm(forms.ModelForm):
    """
    form for adding a new car details
    """

    class Meta:
        """
        Meta class
        """

        model = Song
        fields = "__all__"

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "artist": forms.TextInput(attrs={"class": "form-control"}),
            "genre": forms.Select(attrs={"class": "form-control"}),
            "duration": forms.NumberInput(attrs={"class": "form-control"}),
        }


class MovieForm(forms.ModelForm):
    """
    form for adding a new movie details
    """

    class Meta:
        """
        Meta class
        """

        model = Movie
        fields = "__all__"

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "director": forms.TextInput(attrs={"class": "form-control"}),
            "release_year": forms.NumberInput(attrs={"class": "form-control"}),
            "rating": forms.Select(attrs={"class": "form-control"}),
        }


class JobPostingForm(forms.ModelForm):
    """
    form for adding a new job details
    """

    class Meta:
        """
        Meta class
        """

        model = JobPosting
        fields = "__all__"

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "company": forms.TextInput(attrs={"class": "form-control"}),
            "location": forms.TextInput(attrs={"class": "form-control"}),
            "employment_type": forms.Select(attrs={"class": "form-control"}),
        }


class CategoryForm(forms.ModelForm):
    """
    form for adding a new category
    """

    class Meta:
        """
        Meta class
        """

        model = Category
        fields = "__all__"

        widgets  = {
            "name" : forms.TextInput(attrs= {"class" : "form-control"})
        }

class ProductForm(forms.ModelForm):
    """
    form for adding a new product details
    """

    class Meta:
        """
        Meta class
        """

        model = Product
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
        }


class ProjectForm(forms.ModelForm):
    """
    form for adding a new project details
    """

    class Meta:
        """
        Meta Class
        """
        model = Project
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs= {"class" : "form-control"}),
            "description" : forms.Textarea(attrs= {"class" : "form-control"}),
        }

class TaskForm(forms.ModelForm):
    """
    form for adding a new task details
    """

    class Meta:
        """
        Meta class
        """

        model = Task
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "project": forms.Select(attrs={"class": "form-control"}),
        }

class PostCategoryForm(forms.ModelForm):
    """
    form for adding a new enrollment details
    """

    class Meta:
        """
        Meta Class
        """

        model = PostCategory
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
        }


class PostForm(forms.ModelForm):
    """
    form for adding a new post details
    """

    class Meta:
        """
        Meta class
        """

        model = Post
        fields = "__all__"

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
        }


class EnrollmentForm(forms.ModelForm):
    """
    form for adding a new enrollment details
    """

    class Meta:
        """
        Meta Class
        """

        model = Enrollment
        fields = "__all__"

        widgets = {
            "student": forms.Select(attrs={"class": "form-control"}),
            "course": forms.Select(attrs={"class": "form-control"}),
            "grade": forms.TextInput(attrs={"class": "form-control"}),
        }


class StudentForm(forms.ModelForm):
    """
    form for adding a new student details
    """

    class Meta:
        """
        Meta Class
        """

        model = Student
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
        }

class CourseForm(forms.ModelForm):
    """
    form for adding a new student details
    """

    class Meta:
        """
        Meta Class
        """

        model = Course
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
        }