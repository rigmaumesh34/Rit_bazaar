# Generated by Django 5.1 on 2024-08-19 02:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentApp', '0008_alter_student_department_alter_student_year_of_study'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='year_of_study',
            new_name='yearofstudy',
        ),
    ]
