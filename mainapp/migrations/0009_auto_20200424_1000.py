# Generated by Django 3.0.5 on 2020-04-24 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_post_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='genre',
            field=models.CharField(max_length=255),
        ),
    ]