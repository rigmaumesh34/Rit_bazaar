# Generated by Django 5.1 on 2024-08-18 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('studentApp', '0006_delete_login_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=15)),
                ('department', models.CharField(choices=[('CSE', 'Computer Science and Engineering'), ('ECE', 'Electronics and Communication Engineering'), ('ME', 'Mechanical Engineering'), ('CE', 'Civil Engineering'), ('EE', 'Electrical Engineering')], max_length=3)),
                ('year_of_study', models.CharField(max_length=9)),
                ('password', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
