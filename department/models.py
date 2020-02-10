from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.
class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Group, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.department.name} {self.user.username}'

    def save(self):
        super().save()
