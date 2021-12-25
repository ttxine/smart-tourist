from django.contrib import messages
from django.shortcuts import redirect

from contact.models import Collaboration
from contact.forms import EmployerApplicationForm, TouristApplicationForm


class HomepageService:

    def _build_context(self):
        return {
            'collaborations': Collaboration.objects.all()[:5],
            'employer_form': EmployerApplicationForm(prefix="employer"),
            'tourist_form': TouristApplicationForm(prefix="tourist")
        }

    def execute(self):
        return self._build_context()


class ApplicationService:

    __slots__ = 'request',

    def __init__(self, request) -> None:
        self.request = request

    def create_application_by_form(self):
        employer_form = EmployerApplicationForm(self.request.POST, prefix="employer")
        tourist_form = TouristApplicationForm(self.request.POST, prefix="tourist")
        if employer_form.is_valid():
            employer_form.save()
            messages.success(self.request, "Ваша заявка принята")
            return redirect("/")
        elif tourist_form.is_valid():
            tourist_form.save()
            messages.success(self.request, "Ваша заявка принята")
            return redirect("/")
        else:
            employer_form = EmployerApplicationForm(prefix="employer")
            tourist_form = TouristApplicationForm(prefix="tourist")
            return redirect("/")
