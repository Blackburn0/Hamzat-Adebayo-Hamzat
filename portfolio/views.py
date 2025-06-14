from django.views.generic import ListView, TemplateView
from .models import *


import bleach

ALLOWED_TAGS = ['p', 'b', 'i', 'u', 'strong', 'em', 'ul', 'ol', 'li', 'br', 'a']
ALLOWED_ATTRIBUTES = {
    'a': ['href', 'title'],
}

class HomeView(ListView):
    model = About
    template_name = 'portfolio/index.html'
    context_object_name = 'about'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        about_queryset = context['about']

        # Sanitize each about_detail
        for obj in about_queryset:
            obj.about_detail = bleach.clean(
                obj.about_detail,
                tags=ALLOWED_TAGS,
                attributes=ALLOWED_ATTRIBUTES,
                strip=True
            )

        context['projects'] = Project.objects.all()
        context['stack'] = Stack.objects.all()
        return context


# class HomeView(ListView):
#     model = About
#     template_name = 'portfolio/index.html'
#     context_object_name = 'about' # assign a name to use in a for loop in template

#     def get_context_data(self, **kwargs): # this function allows me to list several objects in models while using a single template
#         context = super().get_context_data(**kwargs) 
#         context['projects'] = Project.objects.all() # This line connect the model you want to add to the List view
#         context['stack'] = Stack.objects.all() # This line connect the model you want to add to the List view

#         return context
    
# class ExperienceView(ListView):
#     model = About
#     template_name = 'portfolio/experience.html'
#     context_object_name = 'about' # assign a name to use in a for loop in template

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['experiences'] = Expereince.objects.all() # This line connect the model you want to add to the List view
#         context['educations'] = Education.objects.all() # This line connect the model you want to add to the List view
#         return context


class ExperienceView(ListView):
    model = About
    template_name = 'portfolio/experience.html'
    context_object_name = 'about'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        about_queryset = context['about']

        # Sanitize each about_detail
        for obj in about_queryset:
            obj.about_detail = bleach.clean(
                obj.about_detail,
                tags=ALLOWED_TAGS,
                attributes=ALLOWED_ATTRIBUTES,
                strip=True
            )

        context['experiences'] = Expereince.objects.all()
        context['educations'] = Education.objects.all()
        return context

   
class ProjectView(ListView):
    model = Project
    template_name = 'portfolio/project.html'
    context_object_name = 'projects'

class TechStackView(ListView):
    model = Stack
    template_name = 'portfolio/tech_stack.html'
    context_object_name = 'stack'


class CertificationView(ListView):
    model = Certification
    template_name = 'portfolio/certification.html'
    context_object_name = 'certifications'
    