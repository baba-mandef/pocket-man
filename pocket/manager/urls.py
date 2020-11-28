from django.urls import path
from pocket.manager.views import home

urlpatterns = [

    path('', home, name='home')

]