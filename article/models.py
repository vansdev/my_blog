from django.db import models

# Create your models here.
from django.core.urlresolvers import reverse


class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True,null=True)
    category = models.CharField(max_length=30,blank=True)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        path = reverse('detail',kwargs={'id':self.id})
        return "http://127.0.0.1:8000%s" % path

    class Meta:
        ordering = ['-date_time']