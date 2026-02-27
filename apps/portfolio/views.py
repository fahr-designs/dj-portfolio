from django.views.generic import TemplateView

from .models import Event, Mix


class HomeView(TemplateView):
    template_name = "portfolio/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["featured_mixes"] = Mix.objects.filter(is_featured=True)[:6]
        context["upcoming_events"] = Event.objects.filter(is_upcoming=True)[:5]
        return context
