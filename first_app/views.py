from django.shortcuts import render
from django.http.response import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect

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
    raise Http404("404 Page Not Found!")

def num_page_view(request, num_page):
  topics_list = list(articles.keys())
  topic = topics_list[num_page]
  return HttpResponseRedirect(topic)