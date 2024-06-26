# Generated by Django 5.0 on 2024-04-26 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='States',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('states', models.CharField(max_length=100)),
                ('cases', models.IntegerField(max_length=100)),
                ('deaths', models.IntegerField(max_length=100)),
                ('recovered', models.IntegerField(max_length=100)),
                ('active', models.IntegerField(max_length=100)),
            ],
            options={
                'db_table': 'States_table',
            },
        ),
    ]
