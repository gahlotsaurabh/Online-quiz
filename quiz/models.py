from django.db import models
from django.contrib.auth.models import User

class Quiz(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Question(models.Model):
    quiz = models.ForeignKey('Quiz',null=False,on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    option1 = models.CharField(max_length=15)
    option2 = models.CharField(max_length=15)
    option3 = models.CharField(max_length=15)
    option4 = models.CharField(max_length=15)
    answer = models.CharField(max_length=15)

    def __str__(self):
        return self.text

class QuizResponse(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_passed = models.BooleanField(default=False)
    attempts = models.IntegerField(default=0)

    def __str__(self):
        return '%s - %s' % (self.quiz, self.user)
