# Generated by Django 4.0.6 on 2022-07-27 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memo',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]