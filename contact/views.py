from django.views.generic import TemplateView

from contact.services import HomepageService, ApplicationService


class HomepageView(TemplateView):
    template_name = "contact/homepage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(HomepageService().execute())
        return context

    def post(self, request, *args, **kwargs):
        return ApplicationService(request).create_application_by_form()


class PrivacyView(TemplateView):
    template_name = "contact/privacy.html"
