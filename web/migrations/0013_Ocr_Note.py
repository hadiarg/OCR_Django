# Generated by Django 3.2.7 on 2021-12-10 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_Ocr_Note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ocr_note',
            name='customer',
        ),
    ]
