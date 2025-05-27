from django.contrib import admin
from .models import BlogPost
from .models import Client
from .models import Partner
from .models import Testimonial, CaseStudy, FAQ
from .models import JobOpening


admin.site.register(BlogPost)
admin.site.register(Client)
admin.site.register(Partner)
admin.site.register(Testimonial)
admin.site.register(CaseStudy)
admin.site.register(FAQ)



@admin.register(JobOpening)
class JobOpeningAdmin(admin.ModelAdmin):
    list_display = ('title', 'experience', 'location', 'is_active')
    list_filter = ('location', 'is_active')
    search_fields = ('title', 'skills')