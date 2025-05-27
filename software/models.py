from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    image = models.ImageField(upload_to='software/blog/', null=True, blank=True)

    def __str__(self):
        return self.title
    

class Client(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='software/clients/', null=True, blank=True)

    def __str__(self):
        return self.name


class Partner(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='software/partners/', null=True, blank=True)

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=150)
    message = models.TextField()
    image = models.ImageField(upload_to='software/testimonials/', null=True, blank=True)

    def __str__(self):
        return self.name

class CaseStudy(models.Model):
    title = models.CharField(max_length=200)
    challenge = models.TextField()
    solution = models.TextField()
    impact = models.TextField()
    image = models.ImageField(upload_to='software/case_study_images/', null=True, blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question
    

# careers page
class JobOpening(models.Model):
    title = models.CharField(max_length=255)
    experience = models.CharField(max_length=100)
    skills = models.TextField()
    location = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)  # For enabling/disabling

    def __str__(self):
        return self.title