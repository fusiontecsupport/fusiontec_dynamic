from django.contrib import admin
from .models import BlogPost, Client, Partner, Testimonial, CaseStudy, FAQ, JobOpening, JobApplication, ContactSubmission

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'post_date', 'short_content', 'has_image')
    list_filter = ('post_date',)
    search_fields = ('title', 'content')

    def short_content(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content
    short_content.short_description = 'Content'

    def has_image(self, obj):
        return bool(obj.image)
    has_image.boolean = True
    has_image.short_description = 'Image?'

# Keep the rest of your admin registrations
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

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject', 'submitted_at')
    list_filter = ('submitted_at',)
    search_fields = ('name', 'email', 'subject', 'message')
    ordering = ('-submitted_at',)
