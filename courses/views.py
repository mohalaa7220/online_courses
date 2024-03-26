
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Course, Section, Level, News,Contact_inf


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
    levels=Level.objects.filter(section=section)
    context = {
        'section': section,
        'levels': levels
    }
    return render(request, 'courses.html', context)
