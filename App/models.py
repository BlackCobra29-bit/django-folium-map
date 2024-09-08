from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=255, blank=False)
    latitude = models.FloatField(null=False)
    longitude = models.FloatField(null=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date Created")

    class Meta:
        verbose_name_plural = "Location"
        ordering = ['-created_at']

    def __str__(self):
        return self.name