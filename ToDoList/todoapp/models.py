from django.db import models

class TodoList(models.Model):
    content = models.TextField()
    
