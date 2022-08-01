from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('ciudades/', views.CiudadesView.as_view()),
    path('ciudades/<int:idCiudad>/', views.getCityById),
    path('habitantes/', views.HabtantesView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)