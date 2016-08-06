from django.core.exceptions import ValidationError
from django.db import models


class Channel(models.Model):
    name = models.CharField("Nome do canal", max_length=255, blank=False, null=False, unique=True)

    class Meta:
        app_label = 'sandrini_test'
        verbose_name = 'Canal'
        verbose_name_plural = 'Canais'

    def __str__(self):
        return self.name

    #TODO: Fix this
    def clean(self, *args, **kwargs):
        if not self.name:
            raise ValidationError('You have not a channel name')
        super(Channel, self).clean(*args, **kwargs)

    def full_clean(self, *args, **kwargs):
        return self.clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.full_clean()

        super().save(*args, **kwargs)


class Product(models.Model):
    name = models.CharField("Nome do produto", max_length=255, blank=False, null=False)
    channel = models.ForeignKey(Channel, verbose_name="Canal")
    sub_product = models.ForeignKey("product", verbose_name="Sub produto", blank=True, null=True)

    class Meta:
        app_label = 'sandrini_test'
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.name