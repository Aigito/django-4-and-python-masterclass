from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound

# Create your views here.

articles = {
  "sports": "Sports Page",
  "finance": "Finance Page",
  "politics": "Politics Page"
}

def news_view(request, topic):
  try:
    result = articles[topic]
    return HttpResponse(result)
  except:
    return HttpResponseNotFound("Page not found for that topic!")
