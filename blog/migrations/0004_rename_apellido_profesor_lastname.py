# Generated by Django 4.0.3 on 2022-04-14 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_lastname_profesor_apellido'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profesor',
            old_name='apellido',
            new_name='lastname',
        ),
    ]