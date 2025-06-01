

from main.models import AdminTheme
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet
from main.serializers import AdminThemeSerializer

class AdminThemeViewSet(viewsets.ModelViewSet):
    queryset = AdminTheme.objects.all()
    serializer_class = AdminThemeSerializer
    permission_classes = [IsAdminUser]
# Create your views here.
