# Generated by Django 3.1.2 on 2020-11-07 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('isbn', models.CharField(max_length=255)),
                ('publisher', models.CharField(max_length=255)),
                ('publication_year', models.DateField(verbose_name='publication year')),
                ('last_modified_date', models.DateField(verbose_name='last modified date')),
                ('created_date', models.DateField(auto_now=True)),
                ('created_at', models.TimeField(auto_now=True)),
                ('update_at', models.TimeField(auto_now=True)),
            ],
        ),
    ]
