# Generated by Django 5.0 on 2024-02-05 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0002_remove_dashboard_user_current_designation'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboard_user',
            name='education',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='dashboard_user',
            name='github',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='dashboard_user',
            name='linkedin',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]