# Generated by Django 2.1.4 on 2019-01-13 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memes', '0005_auto_20190113_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meme',
            name='image',
            field=models.ImageField(blank=True, upload_to='run'),
        ),
    ]
