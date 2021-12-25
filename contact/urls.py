from django.urls import path

from contact.views import HomepageView, PrivacyView

urlpatterns = [
    path("", HomepageView.as_view(), name="homepage"),
    path("privacy", PrivacyView.as_view(), name="privacy")
]
