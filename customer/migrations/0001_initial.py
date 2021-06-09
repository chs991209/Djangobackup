# Generated by Django 3.2 on 2021-06-09 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=64, verbose_name='PASSWORD')),
                ('registered_date', models.DateTimeField(auto_now_add=True, verbose_name='CUSTOMER_REGISTERED_DATE')),
            ],
            options={
                'verbose_name': 'CUSTOMER',
                'verbose_name_plural': 'CUSTOMER',
                'db_table': 'NewProject_customer',
            },
        ),
    ]
