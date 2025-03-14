from django.db import models

# Create your models here.
class NewsCategory(models.Model):
    category_name = models.CharField(max_length=32)
    pub_date = models.DateTimeField("date published")


    def __str__(self):
        return str(self.category_name)


class News(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    category_id = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media',default='')
    date = models.DateTimeField()


