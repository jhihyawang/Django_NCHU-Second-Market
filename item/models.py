from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=250)
    pub_time = models.DateTimeField(default=timezone.now)
    class Meta:
        ordering=('pub_time',)
    def __str__(self):
        return self.name
    
class Item(models.Model):
    category = models.ForeignKey(Category,related_name='items',on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True,null=True)
    price = models.FloatField()
    STATUS = (
        ('5','全新'),
        ('4','幾乎全新'),
        ('3','狀況良好'),
        ('2','輕度使用'),
        ('1','狀況尚可'),
        ('0','免費送出'),
    )
    status = models.CharField(max_length=1,choices=STATUS,default='5')
    hit = models.IntegerField(default=0)
    image = models.ImageField(upload_to= 'item_images',blank=True,null=True,default='item_images/default.png')
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User,related_name='items',on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    class Meta:
        ordering=('-created_at',)
    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)