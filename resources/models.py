from django.db import models

class PYQ(models.Model):
    subject = models.CharField(max_length=200)
    year = models.IntegerField()
    file = models.FileField(upload_to='pyqs/')

    def __str__(self):
        return f'{self.subject} - {self.year}'

class QuestionBank(models.Model):
    subject = models.CharField(max_length=200)
    topic = models.CharField(max_length=200)
    file = models.FileField(upload_to='question_banks/')

    def __str__(self):
        return f'{self.subject} - {self.topic}'

class Solution(models.Model):
    question_bank = models.ForeignKey(QuestionBank, on_delete=models.CASCADE)
    file = models.FileField(upload_to='solutions/')

    def __str__(self):
        return f'Solution for {self.question_bank}'

class EBook(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    file = models.FileField(upload_to='ebooks/')

    def __str__(self):
        return self.title
