from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy , reverse
from django.views.generic import CreateView , UpdateView

from services.services import send_newpassword
from users.models import User
from users.forms import UserRegisterForm , UserProfileForm
from django.conf import settings
import random

class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        new_user = form.save()
        send_mail(
            subject="Поздравляем с успешной регистрацией!",
            message='Добро пожаловать на нашу платформу!',
            from_email = settings.EMAIL_HOST_USER,
            recipient_list= [new_user.email]
        )
        return super().form_valid(form)

class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self,queryset=None):
        return self.request.user


def generate_new_password(request):
    new_password = ''.join([str(random.randint(0,9)) for _ in range(8)])
    request.user.set_password(new_password)
    request.user.save()
    send_newpassword(request.user.email,new_password)
    return redirect(reverse('services:home'))