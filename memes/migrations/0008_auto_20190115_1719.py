# Generated by Django 2.1.4 on 2019-01-15 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memes', '0007_auto_20190115_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meme',
            name='add_date',
            field=models.DateField(),
        ),
    ]
