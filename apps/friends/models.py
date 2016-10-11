from django.db import models

# Create your models here.
class User(models.Model):
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Friendship(models.Model):
	user = models.ForeignKey(User, related_name="user_friendships")
	friend = models.ForeignKey(User, related_name="friend_friendships")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)