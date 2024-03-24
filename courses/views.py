
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Course, Section, Level, News


def home_page(request):
  
    if request.LANGUAGE_CODE == 'en':
        news = News.objects.all().values('news_title', 'news_desc', 'news_date', 'newsImage', 'lessonsNum')
    else:
        news = News.objects.all().values('news_titleinA', 'news_descinA', 'news_date', 'newsImage', 'lessonsNum')
    
    context = {
        'news': news,
    }
    return render(request, 'home.html', context)

# ============ get section and related levels =============
def section_detail(request, section_slug):

    section = get_object_or_404(
        Section.objects.select_related('course').prefetch_related('level_set'),
        section_Slug=section_slug
    )

    context = {
        'section': section,
        'levels': section.level_set.all()
    }
    return render(request, 'courses.html', context)
