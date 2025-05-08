import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from blog.routing import websocket_urlpatterns  # Исправляем импорт

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mini_blog.settings')  # Убедитесь, что путь указан правильно

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns  # Убедитесь, что websocket_urlpatterns определен
        )
    ),
})