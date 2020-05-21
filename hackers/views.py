from django.views.generic import ListView
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Link

# Create your views here.
# def home(request):
	# return render(request, 'hackers/home.html')

class LinkList(ListView):
	model = Link


def link(request, pk):
	user = request.user
	link = get_object_or_404(Link, pk=pk)
	return JsonResponse({
		'likes': link.likes.count(),
		'dislikes': link.dislikes.count(),
		'status': user.is_authenticated,
	})

@login_required
def like(request, pk):
	user = request.user
	link = get_object_or_404(Link, pk=pk)
	if user in link.dislikes.all():
		link.dislikes.remove(user)
		link.likes.add(user)
	elif user in link.likes.all():
		link.likes.remove(user)
	else:
		link.likes.add(user)
	return redirect("hackers:home")
@login_required
def dislike(request, pk):
	user = request.user
	link = get_object_or_404(Link, pk=pk)
	if user in link.likes.all():
		link.likes.remove(user)
		link.dislikes.add(user)
	elif user in link.dislikes.all():
		link.dislikes.remove(user)
	else:
		link.dislikes.add(user)
	return redirect("hackers:home")