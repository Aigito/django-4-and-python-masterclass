from django.shortcuts import render

# Create your views here.
def example_view(request):
  return render(request, 'my_app/example.html')

def variable_view(request):

  my_var = {
    "first_name": "DYLAN",
    "last_name": "pee",
    "some_list": [1, 2, 3],
    "user_logged_in": True,
    "age": 30
  }

  return render(request, 'my_app/variable.html', context = my_var)