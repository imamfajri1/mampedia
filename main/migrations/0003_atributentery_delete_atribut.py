# Generated by Django 5.1.1 on 2024-09-14 13:58

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_atribut_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='AtributEntery',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('time', models.DateField(auto_now_add=True)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Atribut',
        ),
    ]
