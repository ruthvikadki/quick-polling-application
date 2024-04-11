# models.py
from django.db import models
from apps.user.models import User

class Poll(models.Model):
    title = models.CharField(max_length = 30, default="")
    question = models.CharField(max_length=200)
    choice1 = models.CharField(max_length = 50, default="")
    choice2 = models.CharField(max_length = 50, default="")
    choice3 = models.CharField(max_length = 50, default="")
    choice4 = models.CharField(max_length = 50, default="")
    deadline = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.title)

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user)



