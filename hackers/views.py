from django.views.generic import ListView
from .models import Link
# from django.shortcuts import render

# Create your views here.
# def home(request):
	# return render(request, 'hackers/home.html')

class LinkList(ListView):
	model = Link