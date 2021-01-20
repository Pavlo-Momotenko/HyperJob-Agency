from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User


# Create your views here.
from main.forms import VacancyCreationForm, ResumeCreationForm
from resume.models import Resume
from vacancy.models import Vacancy


class IndexView(View):
    def post(self, request):
        n = 0
        form_data = VacancyCreationForm(request.POST)

        if form_data is None:
            n = 1
            form_data = ResumeCreationForm(request.POST)
        if form_data.is_valid():
            data = form_data.cleaned_data
            if n == 0:
                new_obj = Vacancy.objects.create(description=data['description'], author=request.user)
            else:
                new_obj = Resume.objects.create(description=data['description'], author=request.user)
            return redirect(request.path)

        return HttpResponse(status=403)

    def get(self, request):
        creation_form = None
        # Manager
        if User.is_staff and request.user.is_authenticated:
            creation_form = VacancyCreationForm()
        # Candidate
        elif request.user.is_authenticated:
            creation_form = ResumeCreationForm()
        return render(request, 'index.html', {'form': creation_form})


class MyLoginView(LoginView):
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    template_name = 'login.html'


class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'signup.html'
