# Generated by Django 3.0.5 on 2020-04-24 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_auto_20200424_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippit',
            field=models.CharField(default='N/a', max_length=255),
        ),
    ]