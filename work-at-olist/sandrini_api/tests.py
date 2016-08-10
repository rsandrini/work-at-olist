from django.test import TestCase, Client


# Create your tests here.
from sandrini_test.models import Channel, Category


class ApiTestCase(TestCase):
    def setUp(self):
        Channel.objects.create(name="Canal Test")
        Channel.objects.create(name="Canal Sandrini")
        category_1 = Category.objects.create(name="test1", channel=Channel.objects.first())
        category_2 = Category.objects.create(name="test2", channel=Channel.objects.first())
        Category.objects.create(name="test1.1", top_category=category_1, channel=Channel.objects.first())
        category_2_1 = Category.objects.create(name="test2.1", top_category=category_2, channel=Channel.objects.first())
        Category.objects.create(name="test2.1.1", top_category=category_2_1, channel=Channel.objects.first())

    def test_url_category_list_status_code(self):
        c = Client()
        response = c.get('/api/v1/categories/')
        self.assertEqual(response.status_code, 200)

    def test_url_channel_list_status_code(self):
        c = Client()
        response = c.get('/api/v1/channels/')
        self.assertEqual(response.status_code, 200)

    def test_url_channel_details_status_code(self):
        c = Client()
        response = c.get('/api/v1/channels/canal-test/')
        self.assertEqual(response.status_code, 200)

    def test_url_category_details_status_code(self):
        c = Client()
        response = c.get('/api/v1/categories/canal-test-test1/')
        self.assertEqual(response.status_code, 200)

    def test_url_channel_details_status_code_not_found(self):
        c = Client()
        response = c.get('/api/v1/channels/test999/')
        self.assertEqual(response.status_code, 404)

    def test_url_category_details_status_code_not_found(self):
        c = Client()
        response = c.get('/api/v1/categories/canal-not-found/')
        self.assertEqual(response.status_code, 404)

    def test_url_channel_details_response(self):
        c = Client()
        response = c.get('/api/v1/channels/canal-test/')
        self.assertEquals(response.json()['name'], "Canal Test")
        self.assertEquals(response.json()['categories'][0]['name'], "test1")

    def test_url_category_details_response(self):
        c = Client()
        response = c.get('/api/v1/categories/canal-test-test1/')
        self.assertEquals(response.json()['name'], 'test1')
        self.assertEquals(response.json()['sub_categories'][0]['name'], 'test1.1')

    def test_url_channel_total_response(self):
        c = Client()
        response = c.get('/api/v1/channels/')
        self.assertEquals(len(response.json()['results']), 2)

    def test_url_channel_detail_total_response(self):
        c = Client()
        response = c.get('/api/v1/channels/canal-test/')
        self.assertEquals(len(response.json()), 3)

    def test_url_category_total_response(self):
        c = Client()
        response = c.get('/api/v1/categories/')
        self.assertEquals(len(response.json()['results']), 2)

    def test_url_category_detail_total_response(self):
        c = Client()
        response = c.get('/api/v1/categories/canal-test-test1/')
        self.assertEquals(len(response.json()['sub_categories']), 1)
