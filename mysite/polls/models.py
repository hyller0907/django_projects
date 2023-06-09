import datetime

from django.db import models
from django.utils import timezone

# A 'Question' has: (1) a question and (2) a publication date
# A 'Choice" has: (1) The text of the choice; (2) vote tally
# -> Each Choice is associated with a question

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    # That tells Django each Choice is related to a single Question. 
    # Django supports all the common database relationships: (1) many-to-one; 
    # (2) many-to-many; (3) one-to-one
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes= models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text


















