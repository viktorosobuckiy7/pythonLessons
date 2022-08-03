from django.db import models
from datetime import date


class Category(models.Model):
    title = models.CharField(unique=True, max_length=50, db_index=True)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ("position",)


class Dish(models.Model):
    title = models.TextField()
    description = models.TextField(blank=True,  default='')
    price = models.DecimalField('USD amount', max_digits=8, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to="", blank=True, null=True)
    category = models.ForeignKey(Category, null=True, related_name='dishes', on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ("category",)


class Events(models.Model):
    title = models.TextField()
    description = models.TextField(blank=True, default='')
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(default='post_image.png', upload_to='', null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ("date",)


class Gallery(models.Model):
    title = models.TextField()
    events = models.ForeignKey(Events, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ("events",)
        