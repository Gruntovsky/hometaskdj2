# Generated by Django 3.1.2 on 2022-10-11 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=20)),
                ('image', models.CharField(max_length=1000)),
                ('release_date', models.CharField(max_length=100)),
                ('lte_exists', models.CharField(max_length=100)),
                ('slug', models.SlugField(verbose_name=models.CharField(max_length=100))),
            ],
        ),
    ]
