from django.contrib import admin
from .models import PYQ, QuestionBank, Solution, EBook

@admin.register(PYQ)
class PYQAdmin(admin.ModelAdmin):
    list_display = ('subject', 'year')
    search_fields = ('subject', 'year')

@admin.register(QuestionBank)
class QuestionBankAdmin(admin.ModelAdmin):
    list_display = ('subject', 'topic')
    search_fields = ('subject', 'topic')

@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    list_display = ('question_bank',)
    search_fields = ('question_bank__subject', 'question_bank__topic')

@admin.register(EBook)
class EBookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    search_fields = ('title', 'author')
