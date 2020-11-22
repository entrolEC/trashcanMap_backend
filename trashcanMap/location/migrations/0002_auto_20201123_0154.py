# Generated by Django 3.1.3 on 2020-11-22 16:54

from django.db import migrations, models
import location.models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trashcan',
            name='description',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='trashcan',
            name='image',
            field=models.FileField(max_length=300, upload_to=location.models.date_upload_to),
        ),
    ]
