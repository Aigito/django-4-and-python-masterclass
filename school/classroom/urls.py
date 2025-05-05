from django.urls import path
from . import views

app_name = "classroom"

urlpatterns = [
    path("", views.HomeView.as_view(), name = "home"),
    path("thank_you/", views.ThankYouView.as_view(), name = "thank_you"),
    path("contact/", views.ContactView.as_view(), name = "contact"),
    path("create_teacher/", views.TeacherCreateView.as_view(), name = "create_teacher"),
    path("list_teacher/", views.TeacherListView.as_view(), name = "list_teacher"),
    path("detail_teacher/<int:pk>", views.TeacherDetailView.as_view(), name = "detail_teacher"),
]
