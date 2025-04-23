from django.db import models

class musician(models.Model):
    fisrt_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth= models.DateField()

    def __str__(self):
        return f"musician(id={self.id}, fisrt_name={self.fisrt_name}, last_name={self.last_name}, birth={self.birth})"

