# Generated by Django 3.1.4 on 2021-02-11 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0012_auto_20210128_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(upload_to='recipe/', verbose_name='recipe image'),
        ),
    ]
