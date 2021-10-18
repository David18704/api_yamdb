# Generated by Django 2.2.16 on 2021-10-17 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0010_auto_20211013_1514'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='title',
            name='genre',
        ),
        migrations.AddField(
            model_name='title',
            name='genre',
            field=models.ManyToManyField(related_name='genre', to='reviews.Genre'),
        ),
    ]
