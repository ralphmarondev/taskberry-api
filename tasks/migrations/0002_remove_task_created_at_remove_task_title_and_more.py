# Generated by Django 5.0.6 on 2024-06-22 23:14

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='task',
            name='title',
        ),
        migrations.AddField(
            model_name='task',
            name='end_time',
            field=models.DateTimeField(default=django.utils.timezone.now, max_length=50),
        ),
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('high', 'High'), ('low', 'Low')], default='low', max_length=4),
        ),
        migrations.AddField(
            model_name='task',
            name='start_time',
            field=models.DateTimeField(default=django.utils.timezone.now, max_length=50),
        ),
    ]
