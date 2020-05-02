from django.urls import path
from .views import ReviewerBioView
from django.views.generic import TemplateView
from django.conf.urls import include


urlpatterns = [
	path('<slug:slug>', ReviewerBioView.as_view(), name='reviewer'),




]