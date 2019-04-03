# Generated by Django 2.1.5 on 2019-02-28 19:21

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('memes', '0018_auto_20190222_0050'),
    ]

    operations = [
        migrations.AddField(
            model_name='meme',
            name='dislikes',
            field=models.ManyToManyField(blank=True, related_name='dislikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='meme',
            name='publication_date',
            field=models.DateField(blank=True, default=datetime.datetime(1999, 8, 1, 0, 0)),
        ),
        migrations.AlterField(
            model_name='meme',
            name='author',
            field=models.CharField(default='anon', max_length=100),
        ),
    ]
