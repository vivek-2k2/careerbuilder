# Generated by Django 4.2.7 on 2024-01-16 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companys', '0006_hiring_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='hiring',
            name='places',
            field=models.TextField(db_column='places', null=True),
        ),
    ]