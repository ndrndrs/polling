from django.contrib import admin

from .models import Question, Choice


class InlineChoices(admin.TabularInline):
    model = Choice
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date Information', {'fields': ['date_add']}), ]

    inlines = [InlineChoices]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
