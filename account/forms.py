from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegisterForm(UserCreationForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.fields['username'].help_text = None
		self.fields['password1'].help_text = None
		self.fields['password2'].help_text = None

	class Meta:
		model = User
		fields = ('username', 'password1', 'password2')