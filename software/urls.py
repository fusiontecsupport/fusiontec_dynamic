from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about_us/', views.about_us, name='about_us'),
    path('career/', views.career, name='career'),
    path('contact/', views.contact, name='contact'),
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
    path('blog/', views.blog_list, name='blog'),

    path('SCM_ERP/', views.SCM_ERP, name='SCM_ERP'),
    path('SOP_ERP/', views.SOP_ERP, name='SOP_ERP'),
    path('CL_ERP/', views.CL_ERP, name='CL_ERP'),
    path('HM_ERP/', views.HM_ERP, name='HM_ERP'),



    
    # ✅ Add this line (assuming you have a view called job_application_form)
    path('apply/', views.career_application, name='job_application_form'),
]

# Serve static and media files
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
