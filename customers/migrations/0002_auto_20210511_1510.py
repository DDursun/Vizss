# Generated by Django 3.2.2 on 2021-05-11 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='logo',
        ),
        migrations.AddField(
            model_name='customer',
            name='loog',
            field=models.ImageField(default='nopicture.png', upload_to='customers'),
        ),
    ]
