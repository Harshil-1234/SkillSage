from django.db import models
import django.utils

# A model gets mapped to a database table

# Create your models here.

class TutorialCategory(models.Model):
    tutorial_category = models.CharField(max_length=200)
    category_summary = models.CharField(max_length=200)
    # it will store the url
    category_slug = models.CharField(max_length=200)
    category_image = models.CharField(max_length=500 , default=1)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.tutorial_category
    
class TutorialSeries(models.Model):
    tutorial_series = models.CharField(max_length=200)
    tutorial_category = models.ForeignKey(TutorialCategory,default=1,verbose_name="Category",on_delete=models.SET_DEFAULT)
    series_summary = models.CharField(max_length=200)
    series_image = models.CharField(max_length=500, default=1)

    class Meta:
        verbose_name_plural = "Series"

    def __str__(self):
        return self.tutorial_series

# Below class makes a table Tutorial in the database
#Columns will be title,content,published etc
class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length=200)
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField("date published",default=django.utils.timezone.now)

    tutorial_series = models.ForeignKey(TutorialSeries,default=1,verbose_name="Series",on_delete=models.SET_DEFAULT)
    tutorial_slug = models.CharField(max_length=200,default=1)

    def __str__(self):
        return self.tutorial_title