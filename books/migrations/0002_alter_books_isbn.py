# Generated by Django 4.2.10 on 2024-02-29 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='isbn',
            field=models.CharField(max_length=13, unique=True),
        ),
    ]
