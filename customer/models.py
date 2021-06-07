from django.db import models


# Create your models here.

class Order(models.Model):
    orderer = models.ForeignKey('customer.Customer', on_delete=models.CASCADE, verbose_name='ORDERER')
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, verbose_name='Order_Prod_NAME')
    quantity = models.IntegerField(verbose_name='QUANTITY')
    registered_date = models.DateTimeField(auto_now_add=True, verbose_name='Ordered_DATE')

    class Meta:
        db_table = 'Shopping_Order'
        verbose_name = 'Order'
        verbose_name_plural = 'Order'














