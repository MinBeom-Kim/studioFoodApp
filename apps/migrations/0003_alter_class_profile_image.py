# Generated by Django 3.2.3 on 2021-05-22 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_alter_class_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='profile_image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='group/image'),
        ),
    ]
