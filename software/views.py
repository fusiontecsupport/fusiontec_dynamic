from django.shortcuts import render
from .models import BlogPost, Client, Partner, Testimonial, CaseStudy 
from .models import FAQ  # Import FAQ model
from .models import JobOpening   # for career page

def home(request):
    # Existing queries
    posts = BlogPost.objects.all()
    clients = Client.objects.all()
    partners = Partner.objects.all()
    testimonials = Testimonial.objects.all()
    case_studies = list(CaseStudy.objects.all().order_by('created_at'))  # Fetch all case studies and split into two roughly equal halves for left and right columns
    mid = (len(case_studies) + 1) // 2
    left_column = case_studies[:mid]
    right_column = case_studies[mid:]

    # Fetch FAQs and optionally split for two columns
    faqs = list(FAQ.objects.all().order_by('created_at'))
    faq_mid = (len(faqs) + 1) // 2
    faqs_left = faqs[:faq_mid]
    faqs_right = faqs[faq_mid:]

    return render(request, 'software/home.html', {
        'posts': posts,
        'clients': clients,
        'partners': partners,
        'testimonials': testimonials,
        'left_column': left_column,  # left_column to context for case study
        'right_column': right_column,   # right_column to context for case study
        'faqs_left': faqs_left,
        'faqs_right': faqs_right,
    })


def career(request):
    jobs = JobOpening.objects.filter(is_active=True)
    return render(request,'software/career.html', {'jobs': jobs})

from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import redirect

def custom_admin_logout(request):
    logout(request)
    messages.success(request, "Logout successfully")
    return redirect('/')


def about_us(request):
    return render(request, 'software/about_us.html')



def contact(request):
    return render(request, 'software/contact.html')

def terms(request):
    return render(request, 'software/terms.html')

def privacy(request):
    return render(request, 'software/privacy.html')