# Generated by Django 2.0.3 on 2018-03-12 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='coordinates',
        ),
    ]
