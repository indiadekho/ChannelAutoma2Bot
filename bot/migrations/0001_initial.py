# Generated by Django 2.2.1 on 2019-05-17 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserSettings',
            fields=[
                ('user_id', models.BigIntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]