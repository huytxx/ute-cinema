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

class Carausel(models.Model):
    image = models.ImageField(upload_to='course_picture')
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


TYPE_CHOICES = {
    ('promotion','Promotion'),
    ('phim','Phim'),
    ('doi_tac','Đối tác'),
}
class Promotion(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='course_picture')
    start_time = models.CharField(max_length=50)
    end_time = models.CharField(max_length=50)
    type = models.CharField(max_length=90, choices=TYPE_CHOICES, default='promotion')

    def __str__(self):
        return self.title
    