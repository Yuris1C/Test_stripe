from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.IntegerField(default=0)  # cents

    def __str__(self):
        return self.name

    def display_price(self):
        return "{0:.2f}".format(self.price / 100)

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'
