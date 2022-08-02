from django.urls import path
from .views import customer, menu, gallery


urlpatterns = [
    path('', customer),
    path('menu', menu),
    path('gallery', gallery),

]