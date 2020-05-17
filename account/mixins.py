from django.shortcuts import redirect

class LoggedInRedirectMixin():
	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('hackers:links')
		return super().dispatch(request, *args, **kwargs)