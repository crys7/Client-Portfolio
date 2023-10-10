# Generated by Django 4.1.7 on 2023-03-08 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('image', models.ImageField(blank=True, default='default.png', upload_to='grid/')),
                ('category', models.CharField(max_length=50)),
            ],
        ),
    ]
