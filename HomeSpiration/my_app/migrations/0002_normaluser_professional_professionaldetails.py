# Generated by Django 5.0.2 on 2024-02-10 07:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NormalUser',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='my_app.user')),
                ('first_name', models.CharField(max_length=30, null=True)),
                ('last_name', models.CharField(max_length=30, null=True)),
                ('phone_number', models.CharField(max_length=15, null=True)),
                ('country', models.CharField(max_length=100, null=True)),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='profile_photos/')),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Professional',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='my_app.user')),
                ('company_name', models.CharField(max_length=100)),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='professional_profile_photos/')),
                ('cover_photo', models.ImageField(blank=True, null=True, upload_to='professional_cover_photos/')),
                ('phone_number', models.CharField(max_length=15)),
                ('country', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=20)),
                ('license_document', models.FileField(blank=True, null=True, upload_to='license_documents/')),
                ('license_number', models.CharField(max_length=100)),
                ('company_verified', models.BooleanField(default=False)),
                ('company_type', models.CharField(choices=[('LB', 'Local Builder'), ('LR', 'Local Retailer'), ('IB', 'International Builder'), ('IR', 'International Retailer')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='ProfessionalDetails',
            fields=[
                ('professional', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='my_app.professional')),
                ('services_offered', models.CharField(blank=True, max_length=255)),
                ('website_link', models.URLField(blank=True, null=True)),
                ('professional_information', models.TextField(blank=True, null=True)),
                ('business_description', models.TextField(blank=True, null=True)),
                ('certifications_and_awards', models.TextField(blank=True, null=True)),
                ('typical_job_cost', models.CharField(blank=True, max_length=100, null=True)),
                ('number_of_projects', models.CharField(max_length=100)),
            ],
        ),
    ]
