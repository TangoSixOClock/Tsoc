# Generated by Django 5.0.2 on 2024-02-15 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tango', '0002_video_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_id',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
