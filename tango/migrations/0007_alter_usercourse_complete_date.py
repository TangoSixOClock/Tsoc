# Generated by Django 5.0.2 on 2024-02-16 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tango', '0006_chapter_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercourse',
            name='complete_date',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]