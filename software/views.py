import mimetypes
from django.shortcuts import render, redirect
from .models import BlogPost, Client, Partner, Testimonial, CaseStudy 
from .models import FAQ  # Import FAQ model
from .models import JobOpening   # for career page
from django.contrib.auth import logout
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from django.conf import settings
from .forms import JobApplicationForm
from django.template.loader import render_to_string

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

def custom_admin_logout(request):
    logout(request)
    messages.success(request, "Logout successfully")
    return redirect('/')

# def career_application(request):
#     if request.method == 'POST':
#         form = JobApplicationForm(request.POST, request.FILES)
#         if form.is_valid():
#             application = form.save()

#             # Prepare admin email
#             admin_subject = "New Job Application Received"
#             admin_body = render_to_string('software/email_template_admin.html', {
#                 'application': application
#             })

#             admin_email = EmailMessage(
#                 subject=admin_subject,
#                 body=admin_body,
#                 from_email=settings.EMAIL_HOST_USER,
#                 to=[settings.EMAIL_HOST_USER],
#             )
#             admin_email.content_subtype = "html"

#             # Attach resume file if uploaded
#             if application.resume:
#                 admin_email.attach(application.resume.name, application.resume.read(), application.resume.file.content_type)

#             admin_email.send()

#             # Optional: send confirmation email to applicant
#             applicant_subject = "Thank you for your application"
#             applicant_message = f"Dear {application.first_name},\n\nThank you for applying for the position of {application.position}. We have received your application and will review it shortly.\n\nBest regards,\nFusiontec Team"
#             send_mail(
#                 subject=applicant_subject,
#                 message=applicant_message,
#                 from_email=settings.EMAIL_HOST_USER,
#                 recipient_list=[application.email],
#                 fail_silently=True,
#             )

#             messages.success(request, "Application submitted successfully!")
#             return redirect('job_application_form')
#         else:
#             messages.error(request, "There was an error with your application. Please check the form.")

#     else:
#         form = JobApplicationForm()

#     return render(request, 'software/career_form.html', {
#         'form': form,
#         'jobs': JobOpening.objects.filter(is_active=True),
#     })
import mimetypes
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib import messages
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import JobApplicationForm
from .models import JobOpening

def career_application(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save()

            # Prepare admin email
            admin_subject = "New Job Application Received"
            admin_body = render_to_string('software/email_template_admin.html', {
                'application': application
            })

            admin_email = EmailMessage(
                subject=admin_subject,
                body=admin_body,
                from_email=settings.EMAIL_HOST_USER,
                to=[settings.EMAIL_HOST_USER],
            )
            admin_email.content_subtype = "html"

            # Attach resume file if uploaded
            if application.resume:
                content_type, encoding = mimetypes.guess_type(application.resume.name)
                if content_type is None:
                    content_type = 'application/octet-stream'
                admin_email.attach(application.resume.name, application.resume.read(), content_type)

            admin_email.send()

            # Prepare user confirmation email using template
            user_subject = "Thank you for your application"
            user_body = render_to_string('software/email_template_user.html', {
                'application': application
            })

            user_email = EmailMessage(
                subject=user_subject,
                body=user_body,
                from_email=settings.EMAIL_HOST_USER,
                to=[application.email],
            )
            user_email.content_subtype = 'html'
            user_email.send(fail_silently=True)

            messages.success(request, "Application submitted successfully!")
            return redirect('job_application_form')
        else:
            messages.error(request, "There was an error with your application. Please check the form.")

    else:
        form = JobApplicationForm()

    return render(request, 'software/career_form.html', {
        'form': form,
        'jobs': JobOpening.objects.filter(is_active=True),
    })



def about_us(request):
    return render(request, 'software/about_us.html')

from django.conf import settings
from django.core.mail import EmailMessage
from django.contrib import messages
from django.shortcuts import render
from .models import ContactSubmission
from django.template.loader import render_to_string

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save to database
        ContactSubmission.objects.create(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message,
        )

        # Prepare email content using your HTML template
        email_html_content = render_to_string('software/contact_form_email.html', {
            'name': name,
            'email': email,
            'phone': phone,
            'subject': subject,
            'message': message,
        })

        try:
            email_msg = EmailMessage(
                subject=f"[Fusiontec Contact] - {subject}",
                body=email_html_content,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[settings.CONTACT_FORM_RECIPIENT],
            )
            email_msg.content_subtype = "html"  # Important for HTML emails
            email_msg.send()
            messages.success(request, 'Your message has been sent successfully.')
        except Exception as e:
            messages.error(request, f'Error sending message: {str(e)}')

    return render(request, 'software/contact.html')


def terms(request):
    return render(request, 'software/terms.html')

def privacy(request):
    return render(request, 'software/privacy.html')