# Generated by Django 5.0.3 on 2024-04-10 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0030_remove_level_video_url_remove_news_image_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='video_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='section',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
