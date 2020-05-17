from django.views.generic import ListView, DeleteView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from hackers.models import Link
from account.forms import RegisterForm
from account.mixins import LoggedInRedirectMixin
# from django.shortcuts import render

# Create your views here.
class LinkList(LoginRequiredMixin, ListView):
	template_name = 'hackers/links.html'
	def get_queryset(self):
		return Link.objects.filter(user=self.request.user)


class LinkDelete(LoginRequiredMixin, DeleteView):
	model = Link
	success_url = reverse_lazy('hackers:links')


class LinkCreate(LoginRequiredMixin, CreateView):
	model = Link
	fields = ("title", "url", "description")
	success_url = reverse_lazy('hackers:links')

	def form_valid(self, form):
		self.obj = form.save(commit=False)
		self.obj.user = self.request.user
		return super(LinkCreate, self).form_valid(form)


class Login(LoggedInRedirectMixin, LoginView):
	pass


class Register(LoggedInRedirectMixin, CreateView):
	form_class = RegisterForm
	template_name = 'registration/register.html'
	success_url = reverse_lazy('hackers:login')


class Logout(LoginRequiredMixin, LogoutView):
	pass