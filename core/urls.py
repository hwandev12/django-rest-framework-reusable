from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view

schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Snippet API",
        default_version='1.0.0',
        description="API documentation of App",
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('app.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('',
         include([
             path('', include(('app.urls'))),
             path('swagger/', schema_view.with_ui('swagger',
                 cache_timeout=0), name="swagger-schema"),
         ])
         ),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
