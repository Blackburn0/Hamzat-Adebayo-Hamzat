from django.urls import path
from .views import HomeView, AboutView, ProjectView, TechStackView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('projects/', ProjectView.as_view(), name='project'),
    path('tech-stack/', TechStackView.as_view(), name='tech-stack'),

]