from django.db import models


# Create your models here.
class Quiz(models.Model):
    quiz_title = models.CharField(max_length=300)
    num_questions = models.IntegerField(default=0)

    def __str__(self):
        return self.quiz_title


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=300)
    question_num = models.IntegerField(default=0)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=300)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text
    

class Code(models.Model):
    name = models.CharField(max_length=300)
    email =  models.CharField(max_length=300)
    token= models.CharField(max_length=8)
    isexpired=models.BooleanField(default=False)
    quizid=models.IntegerField(default=0)

    def __str__(self):
        return self.token

class Candidate(models.Model):
    email = models.CharField(max_length=300)
    quiz_name = models.CharField(max_length=300)
    token = models.CharField(max_length=8)
    name = models.CharField(max_length=300)
    total_qn = models.IntegerField(default=0)
    correct_qn = models.IntegerField(default=0)
    wrong_qn = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.email