# Generated by Django 3.2.7 on 2021-12-09 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_Ocr_Note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ocr_note',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='ocr_note',
            name='ocr_text',
        ),
        migrations.RemoveField(
            model_name='ocr_note',
            name='ocr_user',
        ),
    ]