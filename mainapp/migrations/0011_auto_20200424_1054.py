# Generated by Django 3.0.5 on 2020-04-24 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_post_snippit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='snippit',
            field=models.CharField(max_length=255),
        ),
    ]
