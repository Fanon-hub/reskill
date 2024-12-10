# Generated by Django 5.0.2 on 2024-12-09 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0010_course_image_course_short_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='image',
        ),
        migrations.AddField(
            model_name='course',
            name='course_image',
            field=models.ManyToManyField(blank=True, related_name='course_image', to='skill.image'),
        ),
    ]
