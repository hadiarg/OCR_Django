# Generated by Django 3.2.7 on 2021-12-03 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ocr_Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ocr_pic', models.ImageField(blank=True, default='ProfilePicture.png', null=True, upload_to='')),
                ('ocr_text', models.CharField(max_length=1000)),
            ],
        ),
    ]
