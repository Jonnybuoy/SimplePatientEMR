# Generated by Django 3.2.14 on 2022-07-28 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visits', '0002_rename_patient_details_visit_patient_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visit',
            old_name='patient_id',
            new_name='patient',
        ),
    ]