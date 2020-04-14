from django.db import models

# Create your models here.

class Log(models.Model):
    method = models.CharField(max_length=10, null=True)
    path = models.CharField(max_length=200, db_index=True)
    status_code = models.PositiveIntegerField(null=True, blank=True)
    response_ms = models.PositiveIntegerField(default=0)

    def __str__(self):
        return '{}  {}'.format(self.method, self.response_ms)

    def final(self):
        return '{}  {} {} {}'.format(self.method, self.path, self.status_code, self.response_ms)    

