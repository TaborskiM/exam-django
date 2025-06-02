from .views import AdminThemeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'themes', AdminThemeViewSet)

urlpatterns = router.urls
