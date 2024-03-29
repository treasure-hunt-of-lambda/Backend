# Generated by Django 2.2.3 on 2019-07-30 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('current_room', models.IntegerField()),
                ('gold', models.IntegerField(default=0)),
                ('inventory', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('errors', models.CharField(max_length=255)),
                ('messages', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.IntegerField()),
                ('title', models.CharField(blank=True, max_length=255)),
                ('description', models.TextField(blank=True)),
                ('coordX', models.IntegerField()),
                ('coordY', models.IntegerField()),
                ('exitN', models.CharField(max_length=255)),
                ('exitE', models.CharField(max_length=255)),
                ('exitS', models.CharField(max_length=255)),
                ('exitW', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
