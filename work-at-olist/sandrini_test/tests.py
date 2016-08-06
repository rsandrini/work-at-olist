from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase
from .models import Channel, Product


class ChannelTestCase(TestCase):
    def setUp(self):
        Channel.objects.create(name="Canal Test")
        Channel.objects.create(name="Canal Sandrini")

    def test_name_str(self):
        channel = Channel.objects.first()
        self.assertEqual(channel.__str__(), "Canal Test")

    def test_empty_name(self):
        with self.assertRaises(ValidationError):
            Channel.objects.create()


class ProductTestCase(TestCase):
    def setUp(self):
        Channel.objects.create(name="Canal Test")
        product_1 = Product.objects.create(name="test1", channel=Channel.objects.first())
        product_2 = Product.objects.create(name="test2", channel=Channel.objects.first())
        Product.objects.create(name="test1.1", sub_product=product_1, channel=Channel.objects.first())
        product_2_1 = Product.objects.create(name="test2.1", sub_product=product_2, channel=Channel.objects.first())
        Product.objects.create(name="test2.1.1", sub_product=product_2_1, channel=Channel.objects.first())

    def test_name_str(self):
        product = Product.objects.first()
        self.assertEqual(product.__str__(), "test1")

    def test_sub_product(self):
        product = Product.objects.get(name="test1.1")
        sub_product = Product.objects.get(name="test1")
        self.assertEqual(product.sub_product, sub_product)

    def test_empty_name(self):
        with self.assertRaises(IntegrityError):
            Product.objects.create()
