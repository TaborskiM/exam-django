# 🧩 Django Admin Theme Manager

Une puissante application Django qui permet le changement dynamique des thèmes du panneau d'administration avec GraphQL, le traitement des tâches en arrière-plan avec Celery, la compilation SCSS et l'analyse de l'accessibilité pour une meilleure expérience utilisateur.

---

## 🚀 Caractéristiques

- 🎨 Changement des thèmes du panneau d'administration de Django via l'API GraphQL
- ⚙️ Prise en charge des tâches d'arrière-plan à l'aide de Celery + Redis
- 🧠 Analyse des thèmes CSS pour des suggestions d'accessibilité
- ✨ Compilation automatique de SCSS en CSS via une tâche Celery
- 📂 Gestion organisée des actifs statiques
- 📊 Suggestions d'amélioration de l'interface utilisateur basées sur l'IA (à venir)

## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/django-admin-theme-manager.git
cd django-admin-theme-manager

### 2. Install Dependencies
pipenv  install -r requirements.txt

🔧 Configuration
dans Django Settings (settings.py)
INSTALLED_APPS = [
    ...
    "graphene_django",
    "django_celery_beat",
    "main",  # your theme manager app
]

GRAPHENE = {
    "SCHEMA": "main.schema.schema",
}
Celery (celery.py)
Assurez-vous que Celery est configuré et fonctionne avec Redis ou votre broker.
celery -A django_exam_final worker --pool=threads --loglevel=INFO

et dans un autre terminal

celery -A exam_django beat --loglevel=INFO

🧬 GraphQL API
taper ce url dans le browser : http://127.0.0.1:8000/graphql/
pour afficher les themes :

query {
    allAdminThemes {
        id
        name
        cssUrl
        isActive
    }
}
Example Mutation to switch theme:

mutation {
    switchTheme(themeId: 3) {
        success
    		activeThemeCssUrl
    		suggestions
    }
}


⚙️ Tâches d'arrière-plan

analyze_theme_accessibility(theme_id) - analyse le CSS du thème actif pour détecter les problèmes d'accessibilité.

compile_scss() - compile SCSS en CSS dans le répertoire statique.

Vous pouvez déclencher ces tâches via GraphQL, les actions de l'administrateur ou le shell de Django :

dans le terminal taper : python manage.py shell 

puis :

from main.tasks import compile_scss
compile_scss.delay()

🧪 Testing
Démarrer Django et Celery :

python manage.py runserver
celery -A yourproject worker -l info

Pour tester la compilation SCSS :

from main.tasks import compile_scss
compile_scss.delay()

Analyser l'accessibilité d'un thème :

from main.tasks import analyze_theme_accessibility
analyze_theme_accessibility.delay(theme_id=3)

🖥️ Personnalisation de l'administration
Modifier admin/base_site.html pour inclure dynamiquement {{ active_theme.css_url }}.

Injecter JS/CSS pour les mises à jour dynamiques.