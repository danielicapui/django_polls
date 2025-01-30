from rest_framework import serializers
from .models import Question, Choice, Post, ChatMessage
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question_text', 'pub_date']
class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'question', 'choice_text', 'votes']
#arquivo serializers.py
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'
class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model= ChatMessage
        fields='__all__'