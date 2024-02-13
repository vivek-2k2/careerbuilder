# Generated by Django 4.2.7 on 2023-12-06 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jobseeker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(db_column='name', null=True)),
                ('dob', models.TextField(db_column='dob', null=True)),
                ('email', models.TextField(db_column='email', null=True)),
                ('mob', models.TextField(db_column='mob', null=True)),
                ('password', models.TextField(db_column='password', null=True)),
            ],
            options={
                'db_table': 'jobseeker_signup',
            },
        ),
    ]
