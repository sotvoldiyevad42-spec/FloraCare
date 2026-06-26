from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Seller, Buyer

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Qo\'shimcha ma\'lumotlar', {'fields': ('role', 'phone_number', 'avatar')}),
    )

admin.site.register(Seller)
admin.site.register(Buyer)