from django.db import models

# Create your models here.

class Deck(models.Model):
    title = models.CharField(max_length=100)
    cardFlipped = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Flashcard(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    deck = models.CharField(max_length=100)

    def __str__(self):
        return self.question
