# Generated by Django 4.1.7 on 2023-04-02 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Palco', '0004_remove_instrumento_nomeinstrumento'),
    ]

    operations = [
        migrations.AddField(
            model_name='instrumento',
            name='quantidade',
            field=models.IntegerField(default='0'),
        ),
    ]
