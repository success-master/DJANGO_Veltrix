from django.db import models

# Create your models here.
import random
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User, Group
from django.urls import reverse

def random_string():
    return str(random.randint(100000, 999999))


STATUS_CHOICES = [('Pending', 'Pending'),
                    ('Progress', 'In Progress'),
                    ('Complete', 'Complete'),
                    ('On Hold', 'On Hold'),
                    ('Cancelled', 'Cancelled')]


# Create your models here.


class Request (models.Model):
    content = models.TextField(max_length = 500)
    date_posted = models.DateTimeField(default=timezone.now)
    ref_code = models.CharField(default=random_string, unique=True, max_length=30, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    author_dept = models.ForeignKey(Group, on_delete=models.CASCADE)
    assign_to = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='AssgnedToGroup')
    editor =models.ForeignKey(User, on_delete=models.CASCADE, related_name='Editor')
    time_edited = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS_CHOICES, default='Pending', max_length=50)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('request_detail', kwargs={'pk': self.pk})
