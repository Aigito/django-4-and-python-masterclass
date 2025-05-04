from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.urls import reverse, reverse_lazy
from .forms import ContactForm

# Create your views here.
class HomeView(TemplateView):
  template_name = "classroom/home.html"

class ThankYouView(TemplateView):
  template_name = "classroom/thank_you.html"

class ContactView(FormView):
  # form class connects to the relevant Form Class
  # Django automatically includes `form` behind the scenes for us to access in the html file
  form_class = ContactForm

  # template_name connects the CBV to the relevant HTML file
  # in FBV this was done by `return render(request, "classroom/contact.html", context = {"form": form})`
  template_name = "classroom/contact.html"

  # success_url = "/classroom/thank_you"
  success_url = reverse_lazy("classroom:thank_you")

  # what to do with the form?
  def form_valid(self, form):
    print(form.cleaned_data)
    return super().form_valid(form)