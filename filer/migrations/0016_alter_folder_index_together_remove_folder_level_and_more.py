# Generated by Django 5.0.dev20230606055133 on 2023-06-07 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0015_alter_file_owner_alter_file_polymorphic_ctype_and_more'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='folder',
            index_together=set(),
        ),
        migrations.RemoveField(
            model_name='folder',
            name='level',
        ),
        migrations.RemoveField(
            model_name='folder',
            name='lft',
        ),
        migrations.RemoveField(
            model_name='folder',
            name='rght',
        ),
        migrations.RemoveField(
            model_name='folder',
            name='tree_id',
        ),
    ]