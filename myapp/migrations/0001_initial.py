# Generated by Django 3.0 on 2020-09-10 10:45

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import myapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_name', models.CharField(max_length=100, unique=True, validators=[django.core.validators.MaxLengthValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='Webpage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, validators=[myapp.models.validate_name])),
                ('url', models.URLField(max_length=100, unique=True)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Topic')),
            ],
        ),
        migrations.CreateModel(
            name='AccessDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('webpage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Webpage')),
            ],
        ),
    ]
