from django.contrib import admin
from .models import Category, Car, Client, Rental, Payment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'model', 'plate_number', 'category', 'price_per_day')
    list_filter = ('category',)
    search_fields = ('brand', 'model', 'plate_number')

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone', 'driver_license')
    search_fields = ('last_name', 'phone', 'driver_license')

@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ('id', 'car', 'client', 'start_date', 'end_date', 'total_price')
    list_filter = ('start_date', 'end_date')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'rental', 'amount', 'payment_date')