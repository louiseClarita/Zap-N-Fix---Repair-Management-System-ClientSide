
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.contrib.auth.models import BaseUserManager



class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True,null="False",default="default@test.com")
    username = models.CharField(max_length=150, unique=True,null="False")
    role = models.CharField(max_length=150, null="False",default="Client")
    number = models.IntegerField()
    location = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=150,unique=False, null="False")
    last_name =models.CharField(max_length=150,unique=False, null="False")
    objects = UserManager()
    date_joined = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(null=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELD = ['id','username','email']


class Repair(models.Model):

    desc = models.TextField()
    createdDate = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,default="Requested")
    repairDate = models.DateField(null=True, blank=True)
    actualRepairDate = models.DateField(null=True, blank=True)
    pricing = models.DecimalField(null=True,max_digits=8, decimal_places=2)
    isDelivery = models.BooleanField(default=False)
    image = models.ImageField(null=True,upload_to='repair_images/', blank=True)
    feedbackRate = models.IntegerField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    product_id = models.ForeignKey('Brand', on_delete=models.CASCADE,null=True)
    user_idClient = models.ForeignKey(User, on_delete=models.CASCADE,null=True, related_name='repairs_client')
    user_idTech = models.ForeignKey(User, on_delete=models.CASCADE,null=True, related_name='repairs_technician')

class Brand(models.Model):
    desc = models.CharField(max_length=50)
    type_id = models.ForeignKey('Type', on_delete=models.CASCADE)

class Type(models.Model):
    desc = models.CharField(max_length=50)

class Component(models.Model):
    desc = models.CharField(max_length=50)

class Problem(models.Model):
    desc = models.CharField(max_length=100)
    type_id = models.ForeignKey(Type, on_delete=models.CASCADE)
    component_id = models.ForeignKey(Component, on_delete=models.CASCADE)

class UserManager(BaseUserManager):
    def create_user(self,  username, email,password=None, **extra_fields):
        if not id:
            raise ValueError('The ID field must be set.')
        if not username:
            raise ValueError('The username field must be set.')
        if not email:
            raise ValueError('The email field must be set.')

        user = self.model(id=id, username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username=None, email =None, password=None,  **extra_fields):
        if username is None:
            username = input("Enter the username: ")
        if email is None:
            email = input("Enter the email: ")

        if extra_fields.get('role') is None:
            extra_fields['role'] = input('Enter role(Tecnician / Client): ')

        if extra_fields.get('location') is None:
            extra_fields['location'] = input('Enter location: ')

        if extra_fields.get('phone') is None:
            extra_fields['phone'] = input('Enter phone: ')
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)