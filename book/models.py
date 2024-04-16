from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(null=True, blank=True)
    rate = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    objects = models.Manager()

    def __str__(self):
        return self.title



