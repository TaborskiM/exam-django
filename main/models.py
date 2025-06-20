from django.db import models
from django.core.validators import URLValidator

# You can use Django's built-in URLValidator as validate_url
validate_url = URLValidator()

# Create your models here.
class AdminTheme(models.Model):
    name = models.CharField(max_length=50, unique=True)
    css_url = models.URLField(blank=True, null=True, validators=[validate_url], help_text="URL du fichier CSS du thème")
    js_url = models.URLField(blank=True, null=True, validators=[validate_url], help_text="URL du fichier JS du thème")
    is_active = models.BooleanField(default=False, verbose_name="Thème activé")
    suggestions = models.TextField(blank=True, null=True)
    def save(self, *args, **kwargs):
        if self.is_active:
            AdminTheme.objects.filter(is_active=True).update(is_active=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name