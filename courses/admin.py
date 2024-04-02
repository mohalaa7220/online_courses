from django.contrib import admin
from .models import (Course, Section, Level, News, Contact_inf, Services)
from django import forms


class SectionAdminForm(forms.ModelForm):
    class Meta:
        model = Section
        exclude = ['section_Slug']


# =============== Course Model =================
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name_en', 'course_name_ar')
    search_fields = ('course_name_en', 'course_name_ar')
    list_filter = ('created_at', 'update_at')


# =============== Section Model =================
@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    form = SectionAdminForm
    list_display = ('section_title_en', 'section_title_ar',
                    'course', 'created_at', 'update_at')
    search_fields = ('section_title_en', 'section_title_ar',
                     'description_en', 'description_ar')
    list_filter = ('created_at', 'update_at')

    readonly_fields = ["image_url"]


# =============== Level Model =================
@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ('level_title_en', 'level_title_ar',
                    'section', 'created_at', 'update_at')
    search_fields = ('level_title_en', 'level_title_ar',
                     'level_description_en', 'level_description_ar')
    list_filter = ('created_at', 'update_at')

    readonly_fields = ["video_url"]


# =============== News Model =================
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('news_title_en', 'news_title_ar', 'news_date',
                    'lessonsNum', 'created_at', 'update_at')
    search_fields = ('news_title_en', 'news_desc_en',
                     'news_title_ar', 'news_desc_ar')
    list_filter = ('created_at', 'update_at')

    readonly_fields = ["image_url"]


# =============== Contact Model =================
@admin.register(Contact_inf)
class Contact_infAdmin(admin.ModelAdmin):
    list_display = ('Phone_Num', 'Email_url', 'Facebook_url', 'Instgram_url',
                    'X_url', 'TikTok_url', 'Telgram_url', 'WhatsUp_url', 'LinkeIN_url')
    search_fields = ('Phone_Num',)


# =============== Services Model =================
@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title_en', 'description_en', 'title_ar', 'description_ar')
    search_fields = ('title_en', 'description_en',
                     'title_ar', 'description_ar')
