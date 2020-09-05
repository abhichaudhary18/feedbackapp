# Generated by Django 3.0.3 on 2020-05-13 17:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0002_delete_messagesend'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sendmessage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=150)),
                ('message', models.TextField(max_length=1500)),
                ('meme', models.ImageField(blank=True, upload_to='')),
            ],
        ),
    ]