"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""
URL configuration for core project.
"""
from django.contrib import admin
from django.urls import path
from inventory.views import server_status_view
from inventory.views import orders
from inventory.views import ProductListAPIView, product_api_detail
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.urls import path, re_path

# Global Schema Meta-Data Information Engine
schema_view = get_schema_view(
   openapi.Info(
      title="Enterprise Inventory Tracking System API",
      default_version='v1',
      description="Production Engine API documentation for managing cross-relational inventory assets, secured via JWT token handshakes.",
      contact=openapi.Contact(email="5845freemusic@gmail.com"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('status/', server_status_view), 
    path('orders/', orders),
    path('api/products/', ProductListAPIView.as_view()),
    path('api/products/<int:pk>/', product_api_detail),
    path('api/token/', TokenObtainPairView.as_view(), name="Token_Obtain"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name="Token_Refresh"),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

