# Generated by Django 5.1 on 2024-09-04 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentApp', '0042_complaints_complaint_type_complaints_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='delete_status',
        ),
    ]
