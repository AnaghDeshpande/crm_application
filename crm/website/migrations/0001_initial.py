# Generated by Django 4.2.20 on 2025-04-13 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now=True)),
                ('first_name', models.TextField(max_length=50)),
                ('last_name', models.TextField(max_length=50)),
                ('email', models.TextField(max_length=50)),
                ('contact', models.TextField(max_length=50)),
                ('address', models.TextField(max_length=50)),
                ('city', models.TextField(max_length=50)),
                ('state', models.TextField(max_length=50)),
            ],
        ),
    ]
