

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('about/', views.about, name='about'),
    path('section-detail/<slug:section_slug>',
         views.section_detail, name='section-detail'),
]
