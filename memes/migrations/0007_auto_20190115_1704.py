# Generated by Django 2.1.4 on 2019-01-15 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memes', '0006_auto_20190113_2351'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AlterField(
            model_name='meme',
            name='add_date',
            field=models.CharField(default='2019/01/01', max_length=100),
        ),
        migrations.AlterField(
            model_name='meme',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
