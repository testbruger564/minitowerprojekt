from django.db import models

# Create your models here.


class hosts(models.Model):
    hostname = models.CharField('Hostname', max_length=50, primary_key=True)
    description = models.TextField('Give a short description', max_length=200, blank=True)

    def __str__(self):
        return self.hostname