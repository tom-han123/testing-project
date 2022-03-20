
from unicodedata import category
from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    category_name=models.CharField(max_length=200)

    def __str__(self):
        return self.category_name 


class Title(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title_name=models.CharField(max_length=200)
    img = models.ImageField(null=True, default="aa.jpg")

    def __str__(self):
        return self.title_name

class Question(models.Model):
    title = models.ForeignKey(Title,on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    
    def __str__(self):
        return self.question_text
    

class Result(models.Model):
    title=models.ForeignKey(Title,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    description=models.TextField()
    min_point=models.IntegerField(default=0) 
    max_point=models.IntegerField(default=0)

    def __str__(self):
        return self.name



class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    points=models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
        