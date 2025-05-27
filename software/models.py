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
    
class JobOpening(models.Model):
    title = models.CharField(max_length=255)
    experience = models.CharField(max_length=100)
    skills = models.TextField()
    location = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)  # For enabling/disabling

    def __str__(self):
        return self.title

class JobApplication(models.Model):
    EXPERIENCE_CHOICES = [
        ("Fresher", "Fresher"),
        ("1-3 Years", "1-3 Years"),
        ("3-5 Years", "3-5 Years"),
        ("5+ Years", "5+ Years"),
        # ("Other", "Other"),
    ]
    STATUS_CHOICES = [
        ("Employed", "Employed"),
        ("Self-Employed", "Self-Employed"),
        ("Unemployed", "Unemployed"),
        ("Student", "Student"),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    linkedin = models.URLField(blank=True, null=True)
    position = models.ForeignKey(JobOpening, on_delete=models.SET_NULL, null=True)
    experience = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES)
    # experience_other = models.CharField(max_length=100, blank=True, null=True)
    employment_status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


#contact form

class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=150)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject} ({self.submitted_at.strftime('%Y-%m-%d %H:%M')})"
