# Generated by Django 4.2.3 on 2023-10-12 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_order_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('csv_file', models.FileField(upload_to='data_reports/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
