# Generated by Django 2.1.5 on 2019-02-21 23:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('memes', '0017_dislike_like'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Dislike',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
        migrations.AddField(
            model_name='meme',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
