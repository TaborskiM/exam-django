from celery import shared_task
import subprocess
import os
from django.conf import settings
import requests
from .models import AdminTheme
import re
import sass

@shared_task(bind=True)
def compile_scss(self, input_path=None, output_path=None):
    """Compile SCSS to CSS with proper path handling"""
    try:
        # Set default paths if not provided
        if not input_path:
            input_path = os.path.join(settings.BASE_DIR, 'static/admin/css.scss')
        if not output_path:
            output_path = os.path.join(settings.BASE_DIR, 'staticfiles/admin/compiled.css')
        
        # Ensure output directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Compile SCSS
        css = sass.compile(filename=input_path)
        
        # Write output
        with open(output_path, 'w') as f:
            f.write(css)
            
        return {
            'status': 'success',
            'input': input_path,
            'output': output_path,
            'message': 'SCSS compiled successfully'
        }
    except Exception as e:
        return {
            'status': 'error',
            'error': str(e),
            'input': input_path,
            'output': output_path
        }

@shared_task(name="themes.tasks.analyze_theme_accessibility")
def analyze_theme_accessibility(theme_id):
    try:
        theme = AdminTheme.objects.get(pk=theme_id)
        css = ""
        response = requests.get(theme.css_url)
        css = response.text

        suggestions = []

        if re.search(r"#ccc|#eee|#fff.*(background|color)", css):
            suggestions.append("Increase contrast for better readability.")
        if "text-transform: uppercase" in css:
            suggestions.append("Use `text-transform` carefully to ensure readability.")
        if ":focus" not in css:
            suggestions.append("Consider styling `:focus` states for accessibility.")

        theme.suggestions = "\n".join(suggestions) or "No issues detected."
        theme.save()
        return f"Suggestions updated for theme '{theme.name}'"

    except AdminTheme.DoesNotExist:
        return "Theme not found"

