# Generated by Django 5.1 on 2024-08-31 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentApp', '0023_alter_events_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(max_length=20),
        ),
    ]
