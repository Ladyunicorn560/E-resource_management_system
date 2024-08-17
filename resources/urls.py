from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pyqs/', views.pyq_list, name='pyq_list'),
    path('question-banks/', views.question_bank_list, name='question_bank_list'),
    path('solutions/', views.solution_list, name='solution_list'),
    path('ebooks/', views.ebook_list, name='ebook_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
