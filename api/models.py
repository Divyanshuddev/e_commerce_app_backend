from django.db import models
import uuid
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=225)
    email = models.EmailField(
        primary_key=True
    )
    password = models.CharField(max_length=225)

    def __str__(self):
        return self.name

class Product(models.Model):
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name= models.CharField(max_length=225)
    rating=models.FloatField(validators=[MinValueValidator(0),MaxValueValidator(5)])
    review=models.PositiveIntegerField(null=False)
    in_stock=models.BooleanField(default=False)
    category_choices = [
    ("Phones", "Phones"),
    ("Computers", "Computers"),
    ("Smart Watch", "Smart Watch"),
    ("Camera", "Camera"),
    ("HeadPhones", "HeadPhones"),
    ("Gaming", "Gaming"),
    ("Women's Fashion", "Women's Fashion"),
    ("Men's Fashion", "Men's Fashion"),
    ("Electronics", "Electronics"),
    ("Home & Lifestyles", "Home & Lifestyles"),
    ("Medicine", "Medicine"),
    ("Sports & Outdoor", "Sports & Outdoor"),
    ("Toys", "Toys"),
    ("Groceries & Pets", "Groceries & Pets"),
    ("Health & Beauty", "Health & Beauty"),
]
    category=models.CharField(max_length=255,choices=category_choices,default="Electronics")
    price=models.PositiveIntegerField(validators=[MinValueValidator(100),MaxValueValidator(10000)],null=False)
    actual_price=models.PositiveIntegerField(validators=[MinValueValidator(100),MaxValueValidator(10000)],null=False)
    discount=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(100)],null=False)
    description=models.CharField(max_length=2000)
    size_choices=(
        ('XS','Extra Small'),
        ('S','Small'),
        ('M','Medium'),
        ('L','Large'),
        ('XL','Extra Large')
    )
    size= models.CharField(max_length=3,choices=size_choices,default="Medium")
    quantity=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)],default=1)
    cart=models.BooleanField(default=False)
    wish_list=models.BooleanField(default=False)
    ordered=models.BooleanField(default=False)
    images=models.JSONField(default=list)
    def __str__(self):
        return self.name