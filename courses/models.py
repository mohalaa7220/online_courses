from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


# ============ course model ================
class Course(models.Model):
    course_name_en = models.CharField(
        max_length=100, verbose_name=_("Course Name"))
    course_name_ar = models.CharField(
        max_length=100, verbose_name=_("اسم الكورس"))
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.course_name_en


# ============ section model ================
class Section(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, verbose_name=_("Course"))
    section_title_en = models.CharField(
        max_length=1000, verbose_name=_("Section Title"))
    section_title_ar = models.CharField(
        max_length=1000, verbose_name=_("اسم القسم"))
    description_en = models.TextField(verbose_name=_("Description"))
    description_ar = models.TextField(verbose_name=_("وصف القسم"))
    pictureSection = models.ImageField(
        upload_to='pictures/', null=True, blank=True, verbose_name=_("Image Section"))
    section_Slug = models.SlugField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.section_title_en

    def save(self, *args, **kwargs):
        if not self.section_Slug:
            self.section_Slug = slugify(self.section_title_en)
        super(Section, self).save()

    class Meta:
        ordering = ('-created_at', '-update_at')


# ============ level model ================
class Level(models.Model):
    level_title_en = models.CharField(
        max_length=100, null=True, verbose_name=_("Level Title"))
    level_title_ar = models.CharField(
        max_length=100, null=True, verbose_name=_("عنوان المستوي"))
    section = models.ForeignKey(
        Section, on_delete=models.CASCADE, verbose_name=_("Section"))
    level_description_en = models.TextField(
        verbose_name=_("Level Description"))
    level_description_ar = models.TextField(verbose_name=_("وصف المستوي"))
   # image_level = models.ImageField(
    #   upload_to='pictures/', null=True, blank=True, verbose_name=_("Image Level"))
   # video = models.FileField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.level_title_en

    class Meta:
        ordering = ('-created_at', '-update_at')


# ============ news model ================
class News(models.Model):

    news_title_en = models.CharField(
        max_length=100, verbose_name=_("News Title"))
    news_desc_en = models.TextField(verbose_name=_("News Description"))
    news_title_ar = models.CharField(
        max_length=100, verbose_name=_("عنوان الخبر"))
    news_desc_ar = models.TextField(verbose_name=_("وصف الخبر"))
    news_date = models.DateField(null=True, blank=True)
    lessonsNum = models.IntegerField(verbose_name=_("Lesson Number"))
    newsImage = models.ImageField(
        upload_to='newsImage/', null=True, blank=True, verbose_name=_("News Image"))
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = "News"
        ordering = ('-created_at', '-update_at')

    def __str__(self):
        return self.news_title_en


# ============ course model =============
class Contact_inf(models.Model):
    Phone_Num = models.CharField(max_length=40, verbose_name=_("phone number"))
    Email_url = models.URLField(null=True, blank=True)
    Facebook_url = models.URLField(null=True, blank=True)
    Instgram_url = models.URLField(null=True, blank=True)
    X_url = models.URLField(null=True, blank=True)
    TikTok_url = models.URLField(null=True, blank=True)
    Telgram_url = models.URLField(null=True, blank=True)
    WhatsUp_url = models.URLField(null=True, blank=True)
    LinkeIN_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.Phone_Num

    class Meta:
        verbose_name = "Contact Information"
        verbose_name_plural = "Contact Information"
