# Generated by Django 5.0 on 2024-09-11 08:09

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_about_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='body',
            field=models.TextField(default=41),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about',
            name='image',
            field=models.ImageField(default=builtins.dir, upload_to='about_images/'),
            preserve_default=False,
        ),
    ]
