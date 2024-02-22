from django.contrib import admin
from .models import Question , Module

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 3

# Register your models here.

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['name','decription', 'num_questions']
    inlines =[QuestionInline]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['pk','quiestion_text','module',
                    'correct']
    list_filter = ['module']