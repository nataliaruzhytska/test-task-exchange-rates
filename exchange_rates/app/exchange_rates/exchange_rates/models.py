from django.db import models
from django.db.models.signals import post_delete, pre_delete
from django.dispatch import receiver
from django.utils import timezone


class Currency(models.Model):
    currency_name = models.CharField(
        choices=[('USD', 'USD'), ('EUR', 'EUR'), ('RUB', 'RUB')],
        max_length=3
    )
    purchase_rate = models.FloatField(
        max_length=10,
        blank=True
    )
    sale_rate = models.FloatField(
        max_length=10,
        blank=True
    )
    date_valid_from = models.DateField(blank=True)
    date_valid_until = models.DateField(blank=True)

    @property
    def get_rate(self):
        return f'{self.currency_name} {self.purchase_rate} {self.sale_rate} {self.date_valid_from} {self.date_valid_until}'

    def __str__(self):
        return self.get_rate

    def save(self, *args, **kwargs):
        currency = Currency.objects.filter(currency_name=self.currency_name).filter(
            date_valid_from__lt=self.date_valid_from).last()
        if currency:
            currency.date_valid_until = self.date_valid_from - timezone.timedelta(days=1)
            currency.save_base()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        queryset = Currency.objects.order_by('date_valid_from').filter(currency_name=self.currency_name)
        currency = queryset.filter(date_valid_from__lt=self.date_valid_from).last()
        currency.date_valid_until = self.date_valid_until
        currency.save_base()
        super().delete()

    class Meta:
        ordering = ['date_valid_from']
        indexes = [
            models.Index(fields=['currency_name', 'date_valid_from', 'date_valid_until']),
        ]

