from django.db import models

# Create your models here.

class Question(models.Model):
    q_text = models.TextField()

    def __str__(self):
        return self.q_text

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    c_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.c_text

class Class(models.Model):
    class_name = models.TextField()
    class_comment = models.TextField()

    def __str__(self):
        return self.class_name

    def is_course_6(self):
        if self.class_name[0] == "6":
            return True
        else:
            return False