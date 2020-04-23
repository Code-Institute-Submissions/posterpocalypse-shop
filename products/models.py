from django.db import models


category_choices = (
    ('Movie Posters', 'Movie Posters'),
    ('Music TV Posters', 'Music TV Posters'),
    ('Art Prints', 'Art Prints'),
)


class Product(models.Model):
    name = models.CharField(max_length=250)
    category = models.CharField(max_length=250, choices=category_choices)
    description = models.TextField()
    artist = models.CharField(max_length=250, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images', blank=True, null=True)

    def __str__(self):
        return self.name