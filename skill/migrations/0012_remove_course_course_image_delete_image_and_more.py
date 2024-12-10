# Generated by Django 5.0.2 on 2024-12-09 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0011_image_remove_course_image_course_course_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='course_image',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.AddField(
            model_name='course',
            name='course_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
