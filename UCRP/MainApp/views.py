from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import *
from .utils import *

class MainMenu(DataMixin, ListView):
    model = PLACES
    template_name = 'MainApp/MainMenu.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))

###############################PLACE###############################

class AddPlace(DataMixin, CreateView):
    form_class = AddPlaceForm
    template_name = 'MainApp/add_post.html'
    success_url = reverse_lazy('MainMenu')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

class ShowPost(DataMixin, DetailView):
    model = PLACES
    template_name = 'MainApp/check_places.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['posts'])
        return dict(list(context.items()) + list(c_def.items()))

###########################EMPLOYEES###############################

class AddEmployee(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddEmployeeForm
    template_name = 'MainApp/add_employee.html'
    success_url = reverse_lazy('MainMenu')
    login_url = '/login/'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавить сотрудника')
        return dict(list(context.items()) + list(c_def.items()))

class ShowEmployees(LoginRequiredMixin, DataMixin, ListView):
    model = Employees
    template_name = 'MainApp/check_employee.html'
    context_object_name = 'employees'
    login_url = '/login/'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        try:
            context['title'] = 'Сотрудники ' + str(context['employees'][0].Svyaz)
        except:
            context['title'] = 'Сотрудники'
        return context

    def get_queryset(self):
        return Employees.objects.filter(Svyaz__slug=self.kwargs['Svyaz_slug'])


##############################EVENTS################################

class AddEvent(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddEventForm
    template_name = 'MainApp/add_event.html'
    success_url = reverse_lazy('MainMenu')
    login_url = '/login/'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавить сотрудника')
        return dict(list(context.items()) + list(c_def.items()))


class ShowEvents(LoginRequiredMixin, DataMixin, ListView):
    model = Events
    template_name = 'MainApp/check_event.html'
    context_object_name = 'event'
    login_url = '/login/'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        try:
            context['title'] = 'События ' + str(context['event'][0].Svyaz)
        except:
            context['title'] = 'События'
        return context

    def get_queryset(self):
        return Events.objects.filter(Svyaz__slug=self.kwargs['Svyaz_slug'])

def pageNotFound(request, exception):
    return render(request, 'MainApp/MainMenu.html', {'posts': posts, 'menu': menu, 'title': 'Главное меню'})

def about(request):
    return HttpResponse("О сайте")


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'MainApp/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('MainMenu')