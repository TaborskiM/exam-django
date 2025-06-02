from rest_framework.authentication import SessionAuthentication
from main.models import AdminTheme
from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets
from main.serializers import AdminThemeSerializer

class AdminThemeViewSet(viewsets.ModelViewSet):
    queryset = AdminTheme.objects.all()
    serializer_class = AdminThemeSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminUser]

