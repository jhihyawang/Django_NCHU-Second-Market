from django.db import models
from django.contrib.auth.models import User
from item.models import Item
# Create your models here.

class Message(models.Model):
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received')
	sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent')
	content = models.TextField()
	pub_time = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('-pub_time',)