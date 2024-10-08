# Generated by Django 5.1 on 2024-09-05 00:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentApp', '0050_delete_claim'),
    ]

    operations = [
        migrations.CreateModel(
            name='Claim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='claims/')),
                ('description', models.TextField()),
                ('lost_location', models.CharField(max_length=25)),
                ('lost_date', models.DateField()),
                ('lost_time', models.TimeField()),
                ('phone_number', models.CharField(max_length=10)),
                ('found_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentApp.founditem')),
            ],
        ),
    ]
