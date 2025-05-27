from django.contrib import admin
from .models import BlogPost
from .models import Client
from .models import Partner
from .models import Testimonial, CaseStudy, FAQ
from .models import JobOpening,JobApplication
from .models import ContactSubmission

admin.site.register(BlogPost)
admin.site.register(Client)
admin.site.register(Partner)
admin.site.register(Testimonial)
admin.site.register(CaseStudy)
admin.site.register(FAQ)
admin.site.register(JobApplication)

@admin.register(JobOpening)
class JobOpeningAdmin(admin.ModelAdmin):
    list_display = ('title', 'experience', 'location', 'is_active')
    list_filter = ('location', 'is_active')
    search_fields = ('title', 'skills')

from django.contrib import admin


@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject', 'submitted_at')
    list_filter = ('submitted_at',)
    search_fields = ('name', 'email', 'subject', 'message')
    ordering = ('-submitted_at',)

