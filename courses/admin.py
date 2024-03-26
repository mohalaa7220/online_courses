from django.contrib import admin
from .models import (Course, Section, Level, News, Contact_inf)
from django.utils.html import format_html
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

    readonly_fields = ["image"]

    def image(self, obj):
        if obj.pictureSection:
            return format_html('<img src="{}" width="500" />'.format(obj.pictureSection.url))
        else:
            return 'No Image'

    image.short_description = 'Display Image'


# =============== Level Model =================
@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ('level_title_en', 'level_title_ar',
                    'section', 'created_at', 'update_at')
    search_fields = ('level_title_en', 'level_title_ar',
                     'level_description_en', 'level_description_ar')
    list_filter = ('created_at', 'update_at')

    readonly_fields = ["image"]

    def image(self, obj):
        if obj.image_level:
            return format_html('<img src="{}" width="500" />'.format(obj.image_level.url))
        else:
            return 'No Image'

    image.short_description = 'Display Image'


# =============== News Model =================
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('news_title_en', 'news_title_ar', 'news_date',
                    'lessonsNum', 'created_at', 'update_at')
    search_fields = ('news_title_en', 'news_desc_en',
                     'news_title_ar', 'news_desc_ar')
    list_filter = ('created_at', 'update_at')

    readonly_fields = ["image"]

    def image(self, obj):
        if obj.newsImage:
            return format_html('<img src="{}" width="500" />'.format(obj.newsImage.url))
        else:
            return 'No Image'

    image.short_description = 'Display Image'


# =============== Contact Model =================
@admin.register(Contact_inf)
class Contact_infAdmin(admin.ModelAdmin):
    list_display = ('Phone_Num', 'Email_url', 'Facebook_url', 'Instgram_url',
                    'X_url', 'TikTok_url', 'Telgram_url', 'WhatsUp_url', 'LinkeIN_url')
    search_fields = ('Phone_Num',)
