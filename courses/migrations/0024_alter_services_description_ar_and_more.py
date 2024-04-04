# Generated by Django 5.0.3 on 2024-04-04 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0023_alter_services_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='description_ar',
            field=models.TextField(verbose_name='وصف الخدمة'),
        ),
        migrations.AlterField(
            model_name='services',
            name='description_en',
            field=models.TextField(verbose_name='Description Title'),
        ),
        migrations.AlterField(
            model_name='services',
            name='title_ar',
            field=models.CharField(max_length=100, verbose_name='عنوان الخدمة'),
        ),
        migrations.AlterField(
            model_name='services',
            name='title_en',
            field=models.CharField(max_length=100, verbose_name='Services Title'),
        ),
    ]
