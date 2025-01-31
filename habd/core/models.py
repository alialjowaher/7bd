from django.db import models
from matplotlib import category

class Category(models.Model):
    name = models.CharField(max_length=255)
    
# Create your models here.

class Question(models.Model):
    class QuestionType(models.TextChoices):
        Text = 'Text'
        Image = 'Image'
        Audio = 'Audio'
        Video = 'Video'
    class RankChoices(models.TextChoices):
        One = '100'
        Two = '200'
        Three = '300'
        Four = '400'
        Five = '500'
    question_type = models.CharField(max_length=255,choices=QuestionType.choices, default=QuestionType.Text)
    text = models.TextField(max_length=2000)
    image = models.ImageField(upload_to='questions/images/',null=True,blank=True)
    audio = models.FileField(upload_to='questions/audio/',null=True,blank=True)
    video = models.FileField(upload_to='questions/video/',null=True,blank=True)
    answer = models.TextField(max_length=2000)
    points = models.CharField(choices=RankChoices.choices,max_length=100,default=RankChoices.One)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    is_selected = models.BooleanField(default=False)
