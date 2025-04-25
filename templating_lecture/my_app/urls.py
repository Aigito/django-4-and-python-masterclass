from django.urls import path
from . import views

# registers the app namespace (app_name is a special keyword that Django looks for)
app_name = "my_app"

urlpatterns = [
  path("", views.example_view, name = "example"),
  path("variable/", views.variable_view, name = "variable")
]