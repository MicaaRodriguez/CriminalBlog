from django.db import models
from cases.models import Case
from django.contrib.auth.models import User


class Comment(models.Model):

    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text