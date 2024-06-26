# Generated by Django 5.0.3 on 2024-03-30 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0019_remove_contact_inf_email_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact_inf',
            name='Email_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contact_inf',
            name='Facebook_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contact_inf',
            name='Instgram_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contact_inf',
            name='LinkeIN_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contact_inf',
            name='Telgram_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contact_inf',
            name='TikTok_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contact_inf',
            name='WhatsUp_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contact_inf',
            name='X_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contact_inf',
            name='Youtube_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
