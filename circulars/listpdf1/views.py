from django.shortcuts import render
from django.http import HttpResponse
from .models import Circulars


# Create your views here.

def homepage(request):
	return render(request=request,
					template_name="listpdf1/home.html",
					context={"Circulars":Circulars.objects.all}
					 )




	#HttpResponse("Hello this works")