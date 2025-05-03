from django import forms
from .models import Review
from django.forms import ModelForm

# class ReviewForm(forms.Form):
#   first_name = forms.CharField(label="First Name", max_length = 100)
#   last_name = forms.CharField(label="Last Name", max_length = 100)
#   # to access the last_name field and apply CSS, we'd have to access the TextInput
#   # eg. widget = forms.TextInput(attrs = { "class": "myform" })
#   email = forms.EmailField(label="Email")
#   review = forms.CharField(
#     label = "Please write your review here",
#     widget = forms.Textarea(attrs={"class": "myform"})
#     # forms.Textarea --> this is how we access the field itself
#     # then we pass the CSS classes through attrs
#   )

class ReviewForm(ModelForm):
  class Meta:
    model = Review
    fields = "__all__"
    labels = {
      "first_name": "What is your first name?",
      "last_name": "Thy family name?",
      "stars": "How was the service?"
    }