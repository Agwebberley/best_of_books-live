# Generated by Django 3.0.5 on 2020-05-01 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0019_reviewers_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewers',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]