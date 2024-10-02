from django.db import models

class Weapon(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)  # نوع السلاح (مسدس، بندقية، إلخ)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    stock = models.IntegerField(default=0)  # الكمية المتاحة
    image = models.ImageField(upload_to='weapon_images/')

    def __str__(self):
        return self.name


class Accessory(models.Model):
    name = models.CharField(max_length=100)
    weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE)  # ربط الإكسسوار بالسلاح
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='accessories/', default='accessories/default.jpg')

    def __str__(self):
        return self.name