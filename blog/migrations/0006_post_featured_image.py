# Generated by Django 4.2.14 on 2024-08-15 17:42

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_rename_post_comment_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
