# Generated by Django 5.1.2 on 2024-11-11 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='library',
            fields=[
                ('serielno', models.IntegerField(primary_key=True, serialize=False)),
                ('book_name', models.CharField(max_length=20)),
                ('authorname', models.CharField(max_length=20)),
                ('subject', models.CharField(max_length=50)),
                ('publisher', models.CharField(max_length=10)),
            ],
        ),
    ]
