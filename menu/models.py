from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0, help_text="Display order (lower = first)")

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='items')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)
    is_veg = models.BooleanField(default=False, verbose_name="Vegetarian")
    is_available = models.BooleanField(default=True, verbose_name="Available")
    is_featured = models.BooleanField(default=False, verbose_name="Featured / Bestseller")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']


    def __str__(self):
        return f"{self.name} - ₹{self.price}"