from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter  # Импортируем SearchFilter
from rest_framework.filters import OrderingFilter  # Импортируем OrderingFilter
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

def root_view(request):
    return render(request, 'blog/root.html', {
        "message": "Welcome to the Mini Blog API!",
        "routes": {
            "posts": "/api/posts/",
            "post_detail": "/api/posts/<id>/",
            "comments": "/api/posts/<post_id>/comments/",
        },
        "documentation": "http://127.0.0.1:8000/api/docs/"
    })

# Представление для списка постов и создания нового поста
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]  # Добавляем OrderingFilter
    filterset_fields = ['author', 'title']  # Фильтрация по автору и названию
    search_fields = ['title', 'content']  # Поиск по названию и содержимому
    ordering_fields = ['created_at', 'title']  # Поля для сортировки
    ordering = ['-created_at']  # Сортировка по умолчанию (по дате создания в обратном порядке)

# Представление для получения, обновления и удаления конкретного поста
class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# Представление для списка комментариев и создания нового комментария
class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['post_id'])

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)