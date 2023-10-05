# Generated by Django 4.2.3 on 2023-09-28 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('profile_picture', models.ImageField(null=True, upload_to='profile_picture/')),
                ('name', models.CharField(max_length=150)),
                ('phone', models.BigIntegerField(null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.PositiveIntegerField()),
                ('address', models.CharField(max_length=200)),
                ('joining_date', models.DateField(null=True)),
                ('is_officeStaff', models.BooleanField(default=False)),
                ('is_deleverystaff', models.BooleanField(default=False)),
                ('is_hubadmin', models.BooleanField(default=False)),
            ],
        ),
    ]