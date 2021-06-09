# Generated by Django 3.2 on 2021-06-09 01:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='QUANTITY')),
                ('registered_date', models.DateTimeField(auto_now_add=True, verbose_name='Ordered_DATE')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer', verbose_name='customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='Order_Prod_NAME')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Order',
                'db_table': 'NewProject_order',
            },
        ),
    ]