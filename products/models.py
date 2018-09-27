from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=50)
    descrption = models.TextField(blank=True,null=True)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    summary = models.TextField(blank=True,null=True)
    featured = models.BooleanField(default=True)

    def __str__(self):
        return '%s, $%s' % (self.title,self.price)
