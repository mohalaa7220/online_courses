# Generated by Django 5.0.3 on 2024-03-29 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0015_alter_level_options_alter_news_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]