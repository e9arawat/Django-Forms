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
    CategoryForm,
    ProjectForm,
    PostCategoryForm,
    StudentForm,
    CourseForm,
)

# Create your views here.


class HomeView(TemplateView):
    """
    Home Vire
    """
    template_name = "myapp/index.html"

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
        context['heading'] = "Book"
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
        context['heading'] = "Car"
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
        context['heading'] = "Song"
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
        context['heading'] = "Movie"
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
        context['heading'] = "Job"
        return context

class AddCategory(CreateView):
    """
    view for displaying categoryForm
    """

    template_name = "myapp/form.html"
    form_class = CategoryForm
    success_url = reverse_lazy("add_product")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = "Category"
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
        context['heading'] = "Product"
        context['add'] = "Add Category"
        context['url_name'] = "add_category"
        return context


    
class AddProject(CreateView):
    """
    view for displaying ProjectForm
    """

    template_name = "myapp/form.html"
    form_class = ProjectForm
    success_url = reverse_lazy("add_task")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = "Project"
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
        context['heading'] = "Task"
        context['add'] = "Add Project"
        context['url_name'] = "add_project"
        return context

class AddPostCategory(CreateView):
    """
    view for displaying PostCategoryForm
    """

    template_name = "myapp/form.html"
    form_class = PostCategoryForm
    success_url = reverse_lazy("add_post")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = "Post Category"
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
        context['heading'] = "Post"
        context['add'] = "Add Category"
        context['url_name'] = "add_post_category"
        return context


class AddStudent(CreateView):
    """
    view for displaying StudentForm
    """

    template_name = "myapp/form.html"
    form_class = StudentForm
    success_url = reverse_lazy("add_enrollment")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = "Student"
        return context
    
class AddCourse(CreateView):
    """
    view for displaying CourseForm
    """

    template_name = "myapp/form.html"
    form_class = CourseForm
    success_url = reverse_lazy("add_enrollment")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = "Course"
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
        context['heading'] = "Enrollment"
        context['add'] = "Add Student"
        context['url_name'] = "add_student"
        context['add2'] = "Add Course"
        context['url_name2'] = "add_course"
        return context
    


    
