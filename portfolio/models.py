from django.db import models

# Create your models here.

class About(models.Model):
    about_detail = models.TextField()

    def __str__(self):
        return self.about_detail

class Expereince(models.Model):
    TYPE = [
        ('Internship', 'Internship'),
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    company_name = models.CharField(max_length=255)
    type = models.CharField(max_length=100, choices=TYPE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title

class Education(models.Model):
    course_name = models.CharField(max_length=255)
    school_name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.school_name

class Project(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Project Image')
    tech_stack = models.CharField(max_length=300)
    source_link = models.URLField(blank=True, null=True)
    live_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class Certification(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Certifications Image')
    live_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title