# Generated by Django 4.2.5 on 2024-04-04 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0002_employee_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='slug',
        ),
    ]
