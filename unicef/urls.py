from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

schema_view = get_schema_view(
    openapi.Info(
        title="Unicef API",
        default_version='v1',
        description="Unicef API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

swagger_urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns = [
    path('unicef/admin/', admin.site.urls),
    path('unicef/api/category/', include('category.urls')),
    path('unicef/api/core/', include('core.urls')),
    path('unicef/api/user/', include('user.urls')),

    path('unicef/', include(swagger_urlpatterns)),
    path('unicef/api/user/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('unicef/api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('unicef/api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
