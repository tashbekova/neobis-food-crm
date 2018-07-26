from __future__ import unicode_literals
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin,BaseUserManager
)
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.conf import settings

class Category(models.Model): 
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True)

    name = models.CharField(max_length=200)
    
    class Meta:
        default_related_name="Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length = 200)

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"

    def __str__(self):
        return self.name

class Meal(models.Model): 
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

    name = models.CharField(max_length=200)
    price=models.CharField(max_length=200)
    description=models.CharField(max_length=400)
    
    class Meta:
        default_related_name="Meal"
        verbose_name_plural = "Meals"

    def __str__(self):
        return self.name

class MealsToOrder(models.Model): 
    meals= models.ForeignKey('Meal', on_delete=models.SET_NULL, null=True)
    orders = models.ForeignKey('Order', on_delete=models.SET_NULL, null=True)

    count = models.IntegerField(default=0)
    
    class Meta:
        default_related_name="MealsToOrder"
        verbose_name_plural = "MealsToOrders"


class Role(models.Model):
    name = models.CharField(max_length = 200)

    class Meta:
        verbose_name = "Role"
        verbose_name_plural = "Roles"

    def __str__(self):
        return self.name

class UserManager(BaseUserManager):
    use_in_migrations = True
 
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given login must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
 
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
 
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password=password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin): 
    role = models.ForeignKey('Role', on_delete=models.SET_NULL, null=True, default=None)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.EmailField(max_length=40, unique=True)
    phone=models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default = False)
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'surname']

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self
    class Meta:
        default_related_name="User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.name

    

class Order(models.Model): 

    users = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    tables= models.ForeignKey('Table', on_delete=models.SET_NULL, null=True)
    is_it_open = models.ForeignKey('Status', on_delete=models.SET_NULL, null=True)
    meals = models.ManyToManyField(Meal,through='MealsToOrder')

    date=models.DateTimeField(auto_now_add=True)  
    class Meta:
        default_related_name="Order"
        verbose_name_plural = "Orders"

class Status(models.Model):
    name = models.CharField(max_length = 200)

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Statuses"

    def __str__(self):
        return self.name

class Table(models.Model):
    name = models.CharField(max_length = 200)

    class Meta:
        verbose_name = "Table"
        verbose_name_plural = "Tables"

    def __str__(self):
        return self.name

class ServicePercentage(models.Model):
    percentages = models.FloatField()
    name='Percentage'
    class Meta:
        verbose_name = 'Percentage'
        verbose_name_plural = 'Percentages'

    def __str__(self):
        return self.name

class Check(models.Model):
    orders=models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    percentages = models.ForeignKey(ServicePercentage, on_delete=models.SET_NULL, null=True)

    date=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'Check'
        verbose_name_plural = 'Checks'
