from django.http.response import HttpResponse

def home_view(request):
  return HttpResponse("HOME PAGE")