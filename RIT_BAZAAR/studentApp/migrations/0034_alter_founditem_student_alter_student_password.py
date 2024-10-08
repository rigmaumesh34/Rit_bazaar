# Generated by Django 5.1 on 2024-09-02 09:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentApp', '0033_alter_events_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='founditem',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='found_items', to='studentApp.student'),
        ),
        migrations.AlterField(
            model_name='student',
            name='password',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
