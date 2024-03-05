"""
Views
"""

from django.urls import reverse_lazy

from django.views.generic import CreateView, TemplateView
from .forms import (
    BookForm,
    CarForm,
    SongForm,
    MovieForm,
    JobPostingForm,
    ProductForm,
    TaskForm,
    PostForm,
    EnrollmentForm,
)

# Create your views here.


class SuccessView(TemplateView):
    """
    View for successful submission
    """

    template_name = "myapp/form-success.html"


class AddBook(CreateView):
    """
    View for displaying BookForm
    """

    template_name = "myapp/form.html"
    form_class = BookForm
    success_url = reverse_lazy("success")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = "Add Book"
        return context


class AddCar(CreateView):
    """
    View for displaying CarForm
    """

    template_name = "myapp/form.html"
    form_class = CarForm
    success_url = reverse_lazy("success")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = "Add Car"
        return context


class AddSong(CreateView):
    """
    View for displaying SongForm
    """

    template_name = "myapp/form.html"
    form_class = SongForm
    success_url = reverse_lazy("success")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = "Add Song"
        return context


class AddMovie(CreateView):
    """
    View for displaying SongForm
    """

    template_name = "myapp/form.html"
    form_class = MovieForm
    success_url = reverse_lazy("success")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = "Add Movie"
        return context


class AddJob(CreateView):
    """
    View for displaying SongForm
    """

    template_name = "myapp/form.html"
    form_class = JobPostingForm
    success_url = reverse_lazy("success")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = "Add Job"
        return context


class AddProduct(CreateView):
    """
    View for displaying ProductForm
    """

    template_name = "myapp/form.html"
    form_class = ProductForm
    success_url = reverse_lazy("success")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = "Add Product"
        return context


class AddTask(CreateView):
    """
    View for displaying TaskForm
    """

    template_name = "myapp/form.html"
    form_class = TaskForm
    success_url = reverse_lazy("success")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = "Add Task"
        return context


class AddPost(CreateView):
    """
    view for displaying Postform
    """

    template_name = "myapp/form.html"
    form_class = PostForm
    success_url = reverse_lazy("success")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = "Add Post"
        return context


class AddEnrollment(CreateView):
    """
    view for displaying EnrollmentForm
    """

    template_name = "myapp/form.html"
    form_class = EnrollmentForm
    success_url = reverse_lazy("success")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = "Add Enrollment"
        return context