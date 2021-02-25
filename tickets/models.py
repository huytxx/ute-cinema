from django.db import models

class Ticket(models.Model):
    name = models.CharField(max_length=1000)
    time = models.CharField(max_length=50)
    release_time = models.CharField(max_length=50)
    description = models.TextField()
    type = models.CharField(max_length=1000)
    fit_for = models.CharField(max_length=100)
    image = models.ImageField(upload_to='course_picture')

    def __str__(self):
        return self.name