from django.db import models
from django.contrib.auth.models import User
#aplicativo blog
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
#aplicativo chatbot
class ChatMessage(models.Model):
    user_message = models.TextField()
    bot_response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_message

# Create your models here.
class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published',auto_now_add=True)
    def __str__(self):
        return self.question_text
class Choice(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
