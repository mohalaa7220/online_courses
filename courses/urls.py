from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('about/', views.about, name='about'),
    path('section-detail/<slug:section_slug>',
         views.section_detail, name='section-detail'),
    path('news_details/<int:news_id>', views.news_details, name='news_details'),
    path('course_details/<int:course_id>',
         views.course_details, name='course_details'),
    path('contact_us/', views.contact_us, name='contact_us'),
]
