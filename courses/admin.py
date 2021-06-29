from django.contrib import admin
from .models import *

# Register your models here.

class choices(admin.StackedInline):
    model = Choice
    extra = 3

class CustomQuestionAdmin(admin.ModelAdmin):
    fields = ['q_text']
    inlines = [choices]

admin.site.register(Question,CustomQuestionAdmin)

admin.site.register(Class)