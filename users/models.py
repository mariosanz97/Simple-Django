from django.db import models

# Create your models here.

class Question(models.Model):
  question_text = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')

class Choice(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)

class Users(models.Model):
  email = models.CharField(max_length=20)
  password = models.CharField(max_length=20)
  def __str__(self):
    template = '{0.email} {0.password}'
    return template.format(self)