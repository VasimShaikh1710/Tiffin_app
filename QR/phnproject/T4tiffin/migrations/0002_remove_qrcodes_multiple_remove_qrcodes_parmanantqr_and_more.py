# Generated by Django 5.1.3 on 2025-01-02 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('T4tiffin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qrcodes',
            name='multiple',
        ),
        migrations.RemoveField(
            model_name='qrcodes',
            name='parmanantqr',
        ),
        migrations.AddField(
            model_name='qrcodes',
            name='multiple_base64',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='qrcodes',
            name='parmanantqr_base64',
            field=models.TextField(blank=True),
        ),
    ]