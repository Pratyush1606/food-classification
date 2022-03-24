# Generated by Django 3.2.12 on 2022-03-24 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kid',
            fields=[
                ('kid_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('kid_name', models.CharField(max_length=100)),
                ('kid_age', models.IntegerField()),
                ('parent_phone_number', models.CharField(max_length=100)),
                ('parent_email_address', models.EmailField(max_length=100)),
            ],
        ),
    ]
