# Generated by Django 2.2.26 on 2022-04-11 13:11

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0014_folder_permission_choices'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('file', '100x100', adapt_rotation=False, allow_fullsize=True, free_crop=True, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping'),
        ),
    ]
