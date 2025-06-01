from .models import AdminTheme

def active_theme(request):
    """
    Retourne le thème actif pour le passer aux templates.
    """
    theme = AdminTheme.objects.filter(is_active=True).first()
    return {'theme': theme}