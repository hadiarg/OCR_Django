# Generated by Django 3.2.7 on 2021-12-07 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_Ocr_Note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ocr_note',
            name='ocr_pic',
            field=models.ImageField(blank=True, default='ProfilePicture.png', null=True, upload_to='static/ocr'),
        ),
    ]
