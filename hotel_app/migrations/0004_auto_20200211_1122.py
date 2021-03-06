# Generated by Django 3.0.3 on 2020-02-11 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_app', '0003_auto_20200206_1552'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='number_of_rooms',
            new_name='room_number',
        ),
        migrations.AlterField(
            model_name='client',
            name='room_number',
            field=models.PositiveIntegerField(),
        ),
    ]
