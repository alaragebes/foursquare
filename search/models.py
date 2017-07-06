from django.db import models

class Word(models.Model):
    word = models.CharField(max_length = 300)
    created_time = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.word
