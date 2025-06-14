from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('experience/', ExperienceView.as_view(), name='experience'),
    path('projects/', ProjectView.as_view(), name='project'),
    path('tech-stack/', TechStackView.as_view(), name='tech-stack'),
    path('certifications/', CertificationView.as_view(), name='certification')
]