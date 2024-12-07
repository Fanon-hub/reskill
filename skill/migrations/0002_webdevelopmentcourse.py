# Generated by Django 5.0.2 on 2024-12-06 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebDevelopmentCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('duration', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
