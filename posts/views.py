import imp
from django.views.generic import ListView
from .models import Post # new


# Create your views here.
class HomePageView(ListView):
    model = Post
    template_name = "home.html"
