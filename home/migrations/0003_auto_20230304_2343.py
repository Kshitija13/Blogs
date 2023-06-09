# Generated by Django 3.2.17 on 2023-03-04 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(default=True, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=True),
            preserve_default=False,
        ),
    ]
