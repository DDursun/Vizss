# Generated by Django 3.2.2 on 2021-05-11 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_auto_20210511_1510'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='loog',
            new_name='log',
        ),
    ]