from django.contrib import admin
from .models import Currency


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('currency_name', 'purchase_rate', 'sale_rate', 'date_valid_from', 'date_valid_until')
    search_fields = ('currency_name', 'purchase_rate', 'sale_rate', 'date_valid_from', 'date_valid_until')
    list_filter = ('currency_name', 'date_valid_from')
