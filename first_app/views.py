from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

articles = {
  "sports": "Sports Page",
  "finance": "Finance Page",
  "politics": "Politics Page"
}

def news_view(request, topic):
  return HttpResponse(articles[topic])
