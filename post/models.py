from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):

    autor = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    title = models.CharField("Titulo", max_length=50)
    text = models.TextField("Texto")
    created_date = models.DateTimeField("fecha de creacion", default = timezone.now())
    published_date = models.DateTimeField("fecha de publicacion", blank = True, null = True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title