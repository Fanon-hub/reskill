# Generated by Django 5.0.2 on 2024-12-07 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0002_webdevelopmentcourse'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={},
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='order',
        ),
    ]
