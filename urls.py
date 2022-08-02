from django.urls import path
from .views import manager, contact, events
from customer.views import menu, gallery


urlpatterns = [
    path('', manager),
    path('menu', menu),
    path('gallery', gallery),
    path('contact', contact),
    path('events', events),
]