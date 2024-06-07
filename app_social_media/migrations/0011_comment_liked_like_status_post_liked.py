# Generated by Django 5.0.6 on 2024-06-06 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_social_media', '0010_alter_like_comment_alter_like_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='liked',
            field=models.ManyToManyField(blank=True, related_name='comment_liked', to='app_social_media.profile'),
        ),
        migrations.AddField(
            model_name='like',
            name='status',
            field=models.CharField(choices=[('like', 'like'), ('unlike', 'unlike')], default='like', max_length=10),
        ),
        migrations.AddField(
            model_name='post',
            name='liked',
            field=models.ManyToManyField(blank=True, related_name='post_liked', to='app_social_media.profile'),
        ),
    ]