# Generated by Django 3.2.17 on 2023-03-04 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_post_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='thumbnail',
        ),
    ]
