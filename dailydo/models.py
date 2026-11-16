from django.db import models
from accounts.models import User

# Create your models here.
class ToDo(models.Model):

    title=models.CharField(max_length=200)

    owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name="todos")

    STATUS_CHOICES=[
        ('pending','pending'),
        ('completed','completed')
    ]

    status=models.CharField(max_length=200,choices=STATUS_CHOICES,default='pending')

    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.title