from django.shortcuts import render

# Create your views here.
def example_view(request):
  return render(request, 'my_app/example.html')

def variable_view(request):

  my_var = {
    "name": "dylan",
    "age": 30
    }

  return render(request, 'my_app/variable.html', context = my_var)