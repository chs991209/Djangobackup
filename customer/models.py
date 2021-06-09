from django.db import models


# Create your models here.

class Customer(models.Model):
    email = models.EmailField()
    password = models.CharField(
        max_length=64, verbose_name='PASSWORD'
    )
    registered_date = models.DateTimeField(auto_now_add=True,
                                           verbose_name='CUSTOMER_REGISTERED_DATE'
                                           )

    class Meta:
        db_table = 'Shopping_CUSTOMER'
        verbose_name = 'CUSTOMER'
        verbose_name_plural = 'CUSTOMER'













