# Generated by Django 3.0.5 on 2020-04-24 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20200424_0904'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='genre',
            field=models.CharField(default='N/a', max_length=255),
        ),
    ]
