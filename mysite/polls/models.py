import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)  # Make text field for question
    pub_date = models.DateTimeField('date published')   # Record question publication date

    def __str__(self):  # This is a built-in method, identifies the instance upon which a method is invoked
        return self.question_text # Return character string

    def was_published_recently(self):  # This is a custom method (member function)
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # Database relationship key
    choice_text = models.CharField(max_length=200) # Make text field for answer choices
    votes = models.IntegerField(default=0) # count number of votes for each choice
    def __str__(self):
        return self.choice_text
