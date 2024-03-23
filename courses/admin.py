from django.contrib import admin
from .models import Course, Section, Level, News
from django import forms
from django.utils.safestring import mark_safe


class SectionAdminForm(forms.ModelForm):
    class Meta:
        model = Section
        exclude = ['section_Slug']


# =============== Course Model =================
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('coursename', 'created_at', 'update_at')
    search_fields = ('coursename',)
    list_filter = ('created_at', 'update_at')


# =============== Section Model =================
@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    form = SectionAdminForm
    list_display = ('sectiontitle', 'course', 'created_at', 'update_at')
    search_fields = ('sectiontitle', 'description',)
    list_filter = ('created_at', 'update_at',)

    readonly_fields = ["image"]

    def image(self, obj):
        if obj.pictureSection:
            return mark_safe('<img src="{url}" width="500" />'.format(url=obj.pictureSection.url))
        else:
            return 'No Image'

    image.short_description = 'Display Image'


# =============== Level Model =================
@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    search_fields = ('levelTitle', 'levelDescription',)
    list_filter = ('created_at', 'update_at',)
    list_display = ('levelTitle', 'section', 'created_at', 'update_at',)
    readonly_fields = ["image"]

    def image(self, obj):
        if obj.image_level:
            return mark_safe('<img src="{url}" width="500" />'.format(url=obj.image_level.url))
        else:
            return 'No Image'

    image.short_description = 'Display Image'


# =============== News Model =================
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    search_fields = ('news_title', 'news_desc',)
    list_filter = ('created_at', 'update_at',)
    list_display = ('news_title', 'news_date', 'lessonsNum',
                    'created_at', 'update_at',)
    readonly_fields = ["image"]

    def image(self, obj):
        if obj.newsImage:
            return mark_safe('<img src="{url}" width="500" />'.format(url=obj.newsImage.url))
        else:
            return 'No Image'

    image.short_description = 'Display Image'
