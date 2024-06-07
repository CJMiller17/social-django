# Generated by Django 5.0.6 on 2024-06-06 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_social_media', '0008_alter_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]