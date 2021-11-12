from django.db import models

# Create your models here.
class Category(models.Model):
    type = models.CharField(max_length=255, null=True)
    class Meta:
        verbose_name_plural = "categories"
    def __str__(self):
        return self.type


class Cast(models.Model):
    name = models.TextField(null=True)
    class Meta:
        verbose_name_plural = "Cast"

    def __str__(self):
        return self.name


class CommonInfo(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    release_date = models.DateField(blank=True)
    categories = models.ManyToManyField(Category,blank=True)
    cast = models.ManyToManyField(Cast,blank=True)
    poster = models.ImageField(upload_to='movie/images')

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

class Movie(CommonInfo):
    pass

class Series(CommonInfo):
    class Meta:
        verbose_name_plural = "Series"

