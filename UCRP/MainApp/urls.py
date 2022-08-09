from django.urls import path
from django.conf.urls.static import static
from django.contrib import admin
from .views import *
from UCRP import settings

urlpatterns = [
    path('', MainMenu.as_view(), name = 'MainMenu'),
    path('', about, name = 'mainpage'),
    path('add_post', AddPlace.as_view(), name = 'add_post'),
    path('add_event', AddEvent.as_view(), name = 'add_event'),
    path('add_employee', AddEmployee.as_view(), name = 'add_employee'),
    path('place/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('show_employees/<slug:Svyaz_slug>/', ShowEmployees.as_view(), name='show_employees'),
    path('show_events/<slug:Svyaz_slug>/', ShowEvents.as_view(), name='show_events'),
    path('login/', LoginUser.as_view(), name='login'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


handler404 = pageNotFound