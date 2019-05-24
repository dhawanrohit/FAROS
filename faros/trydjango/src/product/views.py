from django.http import HttpResponse
from django.shortcuts import render

from .models import Product
from .forms import ProductForm

# Create your views here.

def product_create_view(request):
  form = ProductForm(request.POST or None)
  if form.is_valid():
    form.save()
    form = ProductForm()

  context = {
      'form': form
  }

  return render(request, "product/product_create.html", context)


def product_detail_view(request):
  obj = Product.objects.get(id=2)
  #context = {
  #  "title": obj.title,
  #   "description": obj.description
  #}
  context = {
    "object":obj
  }
  return render(request, "products/details1.html", context)






def home_view(request, *args, **kwargs):
  #return HttpResponse("<h1>Hello World</h1>")
  return render(request, "home.html", {})

def contact_view(*args, **kwargs):
  return HttpResponse("<h1>Contacts Page</h1>")

def about_view(request, *args, **kwargs):
  my_context = {
    "my_text": "This is about us",
    "my_number":123456,
    "my_list":["12345", "213472389", "298734982", "984230948092"]
  }

  return render(request, "about.html", my_context)