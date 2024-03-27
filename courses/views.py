
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import (Course, Section, Level, News, Contact_inf)


# ============ home page =============
def home_page(request):

    news = News.objects.all()

    context = {
        'news': news,
    }
    return render(request, 'home.html', context)


# ============ about page =============
def about(request):
    return render(request, 'about.html')


# ============ course page =============
def contact_us(request):
    contact = Contact_inf.objects.all()
    return render(request, 'contact_us.html', {'contact': contact})


# ============ get section and related levels =============
def section_detail(request, section_slug):

    section = get_object_or_404(
        Section.objects.select_related('course').prefetch_related('level_set'),
        section_Slug=section_slug
    )
    levels = Level.objects.filter(section=section)
    context = {
        'section': section,
        'levels': levels
    }
    return render(request, 'courses.html', context)


# ============ get news details =============
def news_details(request, news_id):

    news_id = get_object_or_404(News.objects.all(), id=news_id)
    context = {
        'news_id': news_id,
    }
    return render(request, 'news_details.html', context)


# ============ get courses details =============
def course_details(request, course_id):

    course_id = get_object_or_404(Level, id=course_id)
    section = course_id.section
    other_levels = section.level_set.exclude(id=course_id.id)
    context = {
        'course_id': course_id,
        'other_levels': other_levels,
    }
    return render(request, 'courses_details.html', context)
