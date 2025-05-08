from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Post, Comment
from django.contrib.auth.models import User

class PostTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.post_data = {'title': 'Test Post', 'content': 'This is a test post.', 'author': self.user.id}
        self.post = Post.objects.create(**self.post_data)

    def test_create_post(self):
        response = self.client.post(reverse('post-list'), self.post_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 2)

    def test_view_post(self):
        response = self.client.get(reverse('post-detail', args=[self.post.id]), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.post.title)

    def test_view_own_posts(self):
        response = self.client.get(reverse('post-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

class CommentTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.post = Post.objects.create(title='Test Post', content='This is a test post.', author=self.user)
        self.comment_data = {'post': self.post.id, 'text': 'This is a test comment.', 'author': self.user.id}
        self.comment = Comment.objects.create(**self.comment_data)

    def test_create_comment(self):
        response = self.client.post(reverse('comment-list'), self.comment_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 2)

    def test_view_own_comments(self):
        response = self.client.get(reverse('comment-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)