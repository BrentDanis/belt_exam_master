from __future__ import unicode_literals
from django.db import models
from django import forms
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
#adding data base structure (think excel headers)

class UsersManager(models.Manager):
	def basic_validator(self, postData):
		errors = {}
		if Users.objects.filter(email=postData['email']).count() > 0:
			errors['email'] = "This email {} already exist".format(postData['email'])
		if len(postData['email']) < 1:
			errors['email']="Email cannot be empty!"
		if len(postData['first_name']) < 2:
			errors['first_name']="First Name must be at least 2 characters."	
		if len(postData['last_name']) < 2:
			errors['last_name']="Last Name must be at least 2 characters."
		if len(postData['password']) < 8:
			errors['password']="Password must be at least 8 characters."
		elif not EMAIL_REGEX.match(postData['email']):
			errors['email']="Invalid Email Address!"

		return errors
	def login_validator(self, postData):
		errors = {}
		check_email = postData['email']
		check_password = postData['password']
		print("\n##################\n", check_email, check_password, "\n##################\n")
		if len(Users.objects.filter(email=check_email)):
			me = Users.objects.get(email=check_email)
		else:
			errors['email'] = "Does not exist"
			return errors
		print me.password
		try:
			clog = bcrypt.checkpw(postData['password'].encode(), (me.password).encode())
		except Exception as e:
			clog = False
		print clog
		if False:
			errors['password'] = "This password is STUPID"
		elif Users.objects.filter(email=postData['email']).count() == 0:
			errors['email'] = "This email {} doesn't exist in our system".format(postData['email'])
		return errors 



class Users(models.Model):
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)
	email=models.EmailField()
	password=models.CharField(max_length=255)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	objects = UsersManager()
	def __str__(self):
		return "\n---------------\nFIRST: {}\nLAST: {}\nEMAIL: {}\nPASSWORD: {}\n---------------\n".format(self.first_name, self.last_name, self.email, self.password)




# put validations here in Models==========================================






