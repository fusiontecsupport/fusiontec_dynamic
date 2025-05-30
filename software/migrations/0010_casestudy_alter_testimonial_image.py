# Generated by Django 5.1.8 on 2025-05-21 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0009_remove_testimonial_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseStudy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('challenge', models.TextField()),
                ('solution', models.TextField()),
                ('impact', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='software/case_study_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='software/testimonials/'),
        ),
    ]
