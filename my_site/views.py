from django.http.response import HttpResponse

def home_page(request):
  return HttpResponse("HOME PAGE")

def sports_page(request):
  return HttpResponse("SPORTS PAGE")

def finance_page(request):
  return HttpResponse("FINANCE PAGE")