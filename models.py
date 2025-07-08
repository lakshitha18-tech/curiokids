from django.db import models
from django.contrib.auth.models import User

class Child(models.Model):
    parent = models.ForeignKey(User, on_delete=models.CASCADE)
    child_name = models.CharField(max_length=100)
    age = models.IntegerField()
    grade = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.child_name} (Grade: {self.grade})"


class Schedule(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    day = models.CharField(max_length=20)
    activity = models.CharField(max_length=100)
    time = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.child.child_name} - {self.day} - {self.activity}"
