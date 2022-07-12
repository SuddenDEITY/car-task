from django.urls import path
from . import views
from .views import CarApiList, car_template_list

urlpatterns = [
        path('api/', CarApiList.as_view(), name='cars_api_list'),
        path('', views.car_template_list, name='cars_list'),

]