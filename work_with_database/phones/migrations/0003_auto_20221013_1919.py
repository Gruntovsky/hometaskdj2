# Generated by Django 3.1.2 on 2022-10-13 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0002_auto_20221013_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='phone',
            name='release_date',
            field=models.DateTimeField(),
        ),
    ]