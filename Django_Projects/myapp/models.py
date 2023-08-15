from django.db import models

# Create your models or class here.
class Contact(models.Model):
	name=models.CharField(max_length=100)  #single line text box
	email=models.EmailField()              #email text box
	mobile=models.PositiveIntegerField()   #positive integer or positive digit text box
	remarks=models.TextField()             #multi line text box
	
	def __str__(self):        #__str__ method is call when the object print.its always return string.
		return self.name
	
class User(models.Model):
	fname=models.CharField(max_length=100)  #single line text box
	lname=models.CharField(max_length=100)  #single line text box
	email=models.EmailField()              #email text box
	mobile=models.PositiveIntegerField()   #positive integer or positive digit text box
	address=models.TextField()             #multi line text box
	gender=models.CharField(max_length=100)  #single line text box
	password=models.CharField(max_length=100)  #single line text box
	profile_pic=models.ImageField(upload_to="profile_pic/")
	
	def __str__(self):
		return self.fname+" "+self.lname


	











































		