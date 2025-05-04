from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import ContactForm

# Create your views here.
class HomeView(TemplateView):
  template_name = "classroom/home.html"

class ThankYouView(TemplateView):
  template_name = "classroom/thank_you.html"

class ContactView(TemplateView):
  # form class connects to the relevant Form Class
  form_class = ContactForm

  # template_name connects the CBV to the relevant HTML file
  # in FBV this was done by `return render(request, "classroom/contact.html", context = {"form": form})`
  template_name = "classroom/contact.html"

