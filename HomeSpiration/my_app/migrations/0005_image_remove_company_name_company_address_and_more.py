# Generated by Django 5.0.2 on 2024-02-13 05:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_company_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phrase', models.CharField(max_length=200)),
                ('ai_image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.RemoveField(
            model_name='company',
            name='name',
        ),
        migrations.AddField(
            model_name='company',
            name='address',
            field=models.CharField(default='Unknown Address', max_length=300),
        ),
        migrations.AddField(
            model_name='company',
            name='company_image',
            field=models.ImageField(blank=True, null=True, upload_to='companies/images/'),
        ),
        migrations.AddField(
            model_name='company',
            name='company_name',
            field=models.CharField(default='Default Company Name', max_length=200),
        ),
        migrations.AddField(
            model_name='company',
            name='company_size',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='company',
            name='completed_projects_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='company',
            name='contact_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='description',
            field=models.TextField(default='No description provided.'),
        ),
        migrations.AddField(
            model_name='company',
            name='ongoing_projects_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='company',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='company',
            name='year_established',
            field=models.IntegerField(default=2022),
        ),
    ]
