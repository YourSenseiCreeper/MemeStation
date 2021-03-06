# Generated by Django 2.1.4 on 2019-01-08 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meme',
            name='add_date',
            field=models.CharField(default='1900/01/01', max_length=100),
        ),
        migrations.AddField(
            model_name='meme',
            name='dislike',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='meme',
            name='image',
            field=models.ImageField(blank=True, upload_to='memes'),
        ),
        migrations.AddField(
            model_name='meme',
            name='like',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='meme',
            name='author',
            field=models.CharField(default='', max_length=100),
        ),
    ]
