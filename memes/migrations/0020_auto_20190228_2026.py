# Generated by Django 2.1.5 on 2019-02-28 19:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memes', '0019_auto_20190228_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meme',
            name='add_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='meme',
            name='publication_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(1999, 8, 1, 0, 0)),
        ),
    ]