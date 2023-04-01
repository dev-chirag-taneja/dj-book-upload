from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    pdf = models.FileField(upload_to="book/pdf/", max_length=100)
    cover = models.ImageField(upload_to="book/cover/", max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)