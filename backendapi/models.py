from django.db import models

# Create your models here.

class Log(models.Model):
    request_type = models.CharField(max_length=30)
    request_path = models.CharField(max_length=30)
    http_status = models.IntegerField()
    time_to_process = models.CharField(max_length=30)

    def __str__(self):
        return self.request_path
    

