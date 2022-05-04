"""final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path
from api.views import get_enchantment, get_guns
from api.views import SkinListAPIView, BlogListAPIView, SkinDetailAPIView, BlogDetailAPIView
from api.views import GraffitiViewSet, CharmViewSet, VisitorViewSet, ManageVisitorViewSet, CharmDetailViewSet, GraffitiDetailViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('guns/', get_guns),
    path('enchantment/', get_enchantment),
    path('skins/', SkinListAPIView.as_view()),
    path('skins/<int:skin_id>/', SkinDetailAPIView.as_view()),
    path('blogs/', BlogListAPIView.as_view()),
    path('blogs/<int:blog_id>/', BlogDetailAPIView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', TokenVerifyView.as_view(), name='token_verify'),
]

router = DefaultRouter()
router.register(r'charms', CharmViewSet, basename='charm')
router.register(r'charmsdetail', CharmDetailViewSet, basename='charm')
router.register(r'graffities', GraffitiViewSet, basename='graffiti')
router.register(r'graffitiesdetail', GraffitiDetailViewSet, basename='graffiti')
router.register(r'visitors', VisitorViewSet, basename='visitor')
router.register(r'manage', ManageVisitorViewSet, basename='manage')

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
