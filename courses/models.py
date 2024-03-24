from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


# ============ course model ================
class Course(models.Model):
    coursename = models.CharField(
        max_length=100, verbose_name=_("Course Name"))
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.coursename


# ============ section model ================
class Section(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, verbose_name=_("Course"))
    sectiontitle = models.CharField(
        max_length=1000, verbose_name=_("Section Title"))
    description = models.TextField(verbose_name=_("Description"))
    pictureSection = models.ImageField(
        upload_to='pictures/', null=True, blank=True, verbose_name=_("Image Section"))
    section_Slug = models.SlugField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.sectiontitle

    def save(self, *args, **kwargs):
        if not self.section_Slug:
            self.section_Slug = slugify(self.sectiontitle)
        super(Section, self).save()


# ============ level model ================
class Level(models.Model):
    levelTitle = models.CharField(
        max_length=100, null=True, verbose_name=_("Level Title"))
    section = models.ForeignKey(
        Section, on_delete=models.CASCADE, verbose_name=_("Section"))
    levelDescription = models.TextField(verbose_name=_("Level Description"))
    image_level = models.ImageField(
        upload_to='pictures/', null=True, blank=True, verbose_name=_("Image Level"))
   # video = models.FileField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.levelTitle


# ============ news model ================
class News(models.Model):

    news_title = models.CharField(max_length=100, verbose_name=_("News Title"))
    news_titleinA = models.CharField(max_length=100, verbose_name=_(" Arabic News Title"))
    news_desc = models.TextField(verbose_name=_("News Description"))
    news_descinA = models.TextField(verbose_name=_("News Description"))
    news_date = models.DateField(null=True, blank=True)
    lessonsNum = models.IntegerField(verbose_name=_("Lesson Number"))
    newsImage = models.ImageField(
        upload_to='newsImage/', null=True, blank=True, verbose_name=_("News Image"))
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = "News"
