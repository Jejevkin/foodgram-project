# Generated by Django 3.1.4 on 2020-12-27 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='ingredient name')),
                ('unit', models.CharField(max_length=64, verbose_name='ingredient unit')),
            ],
        ),
    ]
