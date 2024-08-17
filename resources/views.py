from django.shortcuts import render
from .models import PYQ, QuestionBank, Solution, EBook

def home(request):
    return render(request, 'resources/home.html')


def pyq_list(request):
    pyqs = PYQ.objects.all()
    return render(request, 'resources/pyq_list.html', {'pyqs': pyqs})

def question_bank_list(request):
    question_banks = QuestionBank.objects.all()
    return render(request, 'resources/question_bank_list.html', {'question_banks': question_banks})

def solution_list(request):
    solutions = Solution.objects.all()
    return render(request, 'resources/solution_list.html', {'solutions': solutions})

def ebook_list(request):
    ebooks = EBook.objects.all()
    return render(request, 'resources/ebook_list.html', {'ebooks': ebooks})
