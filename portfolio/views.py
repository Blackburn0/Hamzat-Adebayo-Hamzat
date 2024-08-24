from django.views.generic import ListView, TemplateView
from .models import About, Project, Expereince, Education, Contact
from django.views.generic.edit import FormView
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import ContactForm


# Create your views here.
class HomeView(ListView):
    model = About
    template_name = 'portfolio/index.html'
    context_object_name = 'about' # assign a name to use in a for loop in template

    def get_context_data(self, **kwargs): # this function allows me to list several objects in models while using a single template
        context = super().get_context_data(**kwargs) 
        context['projects'] = Project.objects.all() # This line connect the model you want to add to the List view
        return context
    
class AboutView(ListView):
    model = About
    template_name = 'portfolio/about.html'
    context_object_name = 'about' # assign a name to use in a for loop in template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['experiences'] = Expereince.objects.all() # This line connect the model you want to add to the List view
        context['educations'] = Education.objects.all() # This line connect the model you want to add to the List view
        return context
    
class ProjectView(ListView):
    model = Project
    template_name = 'portfolio/project.html'
    context_object_name = 'projects'

class TechStackView(TemplateView):
    template_name = 'portfolio/tech_stack.html'