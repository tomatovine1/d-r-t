# Generated by Django 3.0.7 on 2020-08-14 20:03

import cloudinary.models
from django.db import migrations, models
import django_better_admin_arrayfield.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Title')),
                ('body', models.TextField(default='', max_length=30000, verbose_name='Text body')),
                ('description', models.TextField(blank=True, help_text="Used to promote this page's content through search engines", max_length=3000, verbose_name='Description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('image', cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='Image')),
                ('image_description', models.TextField(blank=True, help_text='Used to help screen readers describe this image to users with compromised vision.', max_length=500, verbose_name='Image description')),
                ('tag', django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.CharField(max_length=200), null=True, size=None, verbose_name='Keyword')),
                ('slug', models.SlugField(max_length=250, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Publication',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('contact_method', models.CharField(choices=[('EMAIL', 'E-mail'), ('WHATSAPP', 'Whatsapp')], default='EMAIL', max_length=300, verbose_name='Contact method')),
                ('contact_info', models.CharField(max_length=300, verbose_name='Contact')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
            ],
            options={
                'verbose_name': 'Subscriber',
            },
        ),
    ]