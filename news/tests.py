from django.test import TestCase
from django.urls import reverse
from .models import Post
# Create your tests here.

class PostModelTest(TestCase):
	def setUp(self):
		Post.objects.create(title='a', text='b')

	def test_text_content(self):
		post= Post.objects.get(id=1)
		expected_objects_title= f'{post.title}'
		expected_objects_text= f'{post.text}'
		self.assertEqual(expected_objects_title, 'a')
		self.assertEqual(expected_objects_text, 'b')

class HomePageViewTest(TestCase):
	def setUp(self):
		Post.objects.create(title='a', text='b')

	def test_views_urls_exists_at_proper_location(self):
		resp = self.client.get('/')
		self.assertEqual(resp.status_code, 200)