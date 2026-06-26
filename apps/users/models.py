from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Roles(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        SELLER = 'SELLER', 'Seller'
        BUYER = 'BUYER', 'Buyer'
        
    role = models.CharField(
        max_length=10, 
        choices=Roles.choices, 
        default=Roles.BUYER,
        verbose_name='Foydalanuvchi roli'
    )
    
    phone_number = models.CharField(
        max_length=15, 
        blank=True, 
        null=True,
        verbose_name='Telefon raqami'
    )
     
    avatar = models.ImageField(
        upload_to='avatars/', 
        blank=True, 
        null=True,
        verbose_name='Profil rasmi'
    )
        
    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
    
class Seller(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        related_name='seller_profile'
    )
    
    shop_name = models.CharField(
        max_length=255, 
        verbose_name='Doʻkon nomi'
    )
    
    shop_description = models.TextField(
        blank=True, 
        null=True, 
        verbose_name='Doʻkon tavsifi'
    )
    
    adress = models.CharField(
        max_length=255, 
        blank=True, 
        null=True, 
        verbose_name='Manzil'
    )
    
    bio = models.TextField(
        blank=True, 
        null=True, 
        verbose_name='Bio'
    )
    
    is_verified = models.BooleanField(
        default=False, 
        verbose_name='Tasdiqlanganmi'
    )
        
    def __str__(self):
        return self.shop_name

class Buyer(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        related_name='Xaridor_profili'
    )
    
    address = models.CharField(
        max_length=255, 
        blank=True, 
        null=True, 
        verbose_name='Manzil'
    )
    
    phone_number = models.CharField(
        max_length=15, 
        blank=True, 
        null=True, 
        verbose_name='Telefon raqami'
    )
        
    def __str__(self):
        return self.user.username