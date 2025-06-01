import graphene
from graphene_django.types import DjangoObjectType
from .models import AdminTheme
from .tasks import analyze_theme_accessibility

# Type GraphQL
class AdminThemeType(DjangoObjectType):
    class Meta:
        model = AdminTheme

# Query pour lister tous les thèmes
class Query(graphene.ObjectType):
    all_admin_themes = graphene.List(AdminThemeType)

    def resolve_all_admin_themes(self, info):
        return AdminTheme.objects.all()

# Mutation pour activer un thème
class SwitchThemeMutation(graphene.Mutation):
    class Arguments:
        theme_id = graphene.ID(required=True)

    success = graphene.Boolean()
    active_theme_css_url = graphene.String()
    suggestions = graphene.String()

    def mutate(self, info, theme_id):
        try:
            # Désactiver tous les thèmes
            AdminTheme.objects.all().update(is_active=False)

            # Activer le thème sélectionné
            theme = AdminTheme.objects.get(id=theme_id)
            theme.is_active = True
            theme.save()

            suggestions_message = analyze_theme_accessibility(theme.id)

            return SwitchThemeMutation(
                success=True,
                active_theme_css_url=theme.css_url,
                suggestions = theme.suggestions
            )
        except AdminTheme.DoesNotExist:
            return SwitchThemeMutation(success=False, active_theme_css_url=None)

# Schéma final
class Mutation(graphene.ObjectType):
    switch_theme = SwitchThemeMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)