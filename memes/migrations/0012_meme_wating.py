# Generated by Django 2.1.5 on 2019-01-23 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memes', '0011_auto_20190115_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='meme',
            name='wating',
            field=models.BooleanField(default=True),
        ),
    ]
