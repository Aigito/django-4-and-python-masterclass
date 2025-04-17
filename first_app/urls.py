from django.urls import path
from . import views

# domain.com/first_app/""
urlpatterns = [
  path("sports",views.sports_view),
  path("finance",views.finance_view)
]