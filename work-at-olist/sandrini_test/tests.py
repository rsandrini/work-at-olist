import os

from django.core.exceptions import ValidationError
from django.core.management import call_command, CommandError
from django.db import IntegrityError
from django.test import TestCase
from django.utils.six import StringIO
from .models import Channel, Category


class ChannelTestCase(TestCase):
    def setUp(self):
        Channel.objects.create(name="Canal Test")
        Channel.objects.create(name="Canal Sandrini")

    def test_name_str(self):
        channel = Channel.objects.first()
        self.assertEqual(channel.__str__(), "Canal Test")

    # def test_empty_name(self):
    #     with self.assertRaises(ValidationError):
    #         Channel.objects.create()


class CategoryTestCase(TestCase):
    def setUp(self):
        Channel.objects.create(name="Canal Test")
        category_1 = Category.objects.create(name="test1", channel=Channel.objects.first())
        category_2 = Category.objects.create(name="test2", channel=Channel.objects.first())
        Category.objects.create(name="test1.1", top_category=category_1, channel=Channel.objects.first())
        category_2_1 = Category.objects.create(name="test2.1", top_category=category_2, channel=Channel.objects.first())
        Category.objects.create(name="test2.1.1", top_category=category_2_1, channel=Channel.objects.first())

    def test_name_str(self):
        category = Category.objects.first()
        self.assertEqual(category.__str__(), "test1")

    def test_sub_category(self):
        category = Category.objects.get(name="test1.1")
        top_category = Category.objects.get(name="test1")
        self.assertEqual(category.top_category, top_category)

    def test_empty_name(self):
        with self.assertRaises(IntegrityError):
            Category.objects.create()


class ImportCommandtest(TestCase):
    path = os.path.dirname(os.path.abspath(__file__))

    def test_command_output_without_parameters(self):
        out = StringIO()
        with self.assertRaises(CommandError):
            call_command('importcategories', stdout=out)

    def test_command_with_invalid_file_path_output(self):
        out = StringIO()
        with self.assertRaises(Exception):
            call_command('importcategories', 'walmart', 'pasta/arquivo.csv', stdout=out)
            self.assertIn('File does not exists', out.getvalue())

    def test_command_import(self):
        out = StringIO()
        call_command('importcategories', 'walmart',
                     '%s/test_file/olist.csv' % self.path, stdout=out)
        self.assertIn('ok', out.getvalue())
        self.assertEqual(Channel.objects.filter(name='walmart').count(), 1)
        self.assertEqual(Category.objects.filter(channel__name='walmart').count(), 23)

    def test_command_invalid_column(self):
        out = StringIO()
        with self.assertRaises(Exception):
            call_command('importcategories', 'walmart',
                     '%s/test_file/olist_invalid.csv' % self.path, stdout=out)
