from django.contrib import admin
from django.urls import path, include
from blog.views import root_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="Mini Blog API",
        default_version="v1",
        description="API documentation for the Mini Blog project",
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path('', root_view, name='root'),  # Корневой маршрут
    path('admin/', admin.site.urls),  # Админ-панель
    path('api/', include('blog.urls')),  # Подключение маршрутов приложения blog
    path('api/docs/', schema_view.with_ui('redoc', cache_timeout=0), name='api-docs'),  # ReDoc UI
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='api-redoc'),  # ReDoc UI
]