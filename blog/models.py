from django.db import models
from django.urls import reverse

# Create your models here.
class Blogs(models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 300)
    description_all = models.TextField()
    data = models.DateField(auto_now = False )
    url = models.URLField()

    def get_absolute_url(self):
        return reverse('detail', kwargs={'blog_id': self.pk})
