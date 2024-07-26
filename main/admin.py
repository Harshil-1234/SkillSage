from django.contrib import admin
from .models import Tutorial,TutorialSeries,TutorialCategory
from django.db import models
from tinymce.widgets import TinyMCE

# Register your models here.

#Now cannot use fields and fieldsets together 
class TutorialAdmin(admin.ModelAdmin):
    #it modifies the position of attributes as mentioned
    # fields = ["tutorial_title",
    #           "tutorial_published",
    #           "tutorial_content"]
    
    #It breaks the attributes in sets
    # Like below 2 sets of 2,1 attributes is created
    fieldsets = [
        ("Title/date",{"fields":["tutorial_title","tutorial_published"]}),
        ("URL",{"fields":["tutorial_slug"]}),
        ("Series",{"fields":["tutorial_series"]}),
        ("Content",{"fields":["tutorial_content"]})
        ]
    
    formfield_overrides = {
        models.TextField: {'widget':TinyMCE()}
    }

#To use the models we created, we have to register them here first
admin.site.register(TutorialSeries)
admin.site.register(TutorialCategory)
admin.site.register(Tutorial,TutorialAdmin)