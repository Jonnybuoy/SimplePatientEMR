# Generated by Django 3.2.14 on 2022-07-28 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0002_auto_20220728_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=255, null=True),
        ),
    ]
