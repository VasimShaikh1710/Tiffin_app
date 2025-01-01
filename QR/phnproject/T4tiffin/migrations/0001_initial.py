# Generated by Django 5.1 on 2024-12-23 16:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='forgotpassword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=10)),
                ('standard', models.CharField(max_length=10)),
                ('division', models.CharField(max_length=10)),
                ('roll_no', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('school_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='StudentRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('student_name', models.CharField(max_length=100)),
                ('parent_name', models.CharField(max_length=100)),
                ('standard', models.CharField(max_length=10)),
                ('division', models.CharField(max_length=10)),
                ('parent_phone', models.CharField(max_length=15)),
                ('roll_no', models.CharField(default='', max_length=100)),
                ('actual_password', models.CharField(default='', max_length=100)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Standards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standard', models.CharField(max_length=10)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='T4tiffin.studentregistration')),
            ],
        ),
        migrations.CreateModel(
            name='Qrcodes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parmanantqr', models.ImageField(blank=True, upload_to='qr_codes/')),
                ('multiple', models.ImageField(blank=True, upload_to='ml_qrcodes/')),
                ('encrypt1', models.CharField(max_length=500)),
                ('encrypt2', models.CharField(max_length=500)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='T4tiffin.studentregistration')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('additional_note', models.CharField(default=None, max_length=100)),
                ('order_status', models.CharField(choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('delivered', 'Delivered'), ('cancelled', 'Cancelled')], default='pending', max_length=100)),
                ('code', models.CharField(default='', max_length=5)),
                ('encrypt', models.CharField(default='', max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('qr_code', models.ImageField(blank=True, upload_to='qr_codes/')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='T4tiffin.studentregistration')),
            ],
        ),
    ]
