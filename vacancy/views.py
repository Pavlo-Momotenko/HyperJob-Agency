from django.shortcuts import render
from vacancy.models import Vacancy
from django.views import View


# Create your views here.
class VacanciesView(View):
    def get(self, request):
        vacancies = Vacancy.objects.all()
        return render(request, 'vacancies.html', {'vacancies': vacancies})
