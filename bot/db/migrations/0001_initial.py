# Generated by Django 3.2.7 on 2021-09-14 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.TextField()),
                ('channel_id', models.TextField()),
                ('message_id', models.TextField()),
                ('message', models.TextField()),
                ('remind_time', models.DateTimeField()),
            ],
        ),
    ]