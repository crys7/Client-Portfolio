# Generated by Django 4.1.7 on 2023-03-08 17:39

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_portfoliodetails_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfoliodetails',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
