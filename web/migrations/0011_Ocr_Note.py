# Generated by Django 3.2.7 on 2021-12-09 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_Ocr_Note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ocr_note',
            name='ocr_pic',
            field=models.ImageField(upload_to='ocr/'),
        ),
    ]
