# Generated by Django 3.0.3 on 2020-05-14 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0007_remove_sendmessage_meme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sendmessage',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
