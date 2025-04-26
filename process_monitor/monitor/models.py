from django.db import models

class Process(models.Model):
    hostname = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    pid = models.IntegerField()
    name = models.CharField(max_length=255)
    cpu = models.FloatField()
    memory = models.FloatField()
    parent_pid = models.IntegerField(null=True, blank=True)
    parent_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.pid})"
