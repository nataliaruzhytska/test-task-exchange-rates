from django.db import models


class Currency(models.Model):
    currency_name = models.CharField(
        choices=[('UAH', 'UAH'), ('USD', 'USD'), ('EUR', 'EUR')],
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
        # if self.get_previous_in_order:
        #     currency = self.get_previous_in_order
        #     if self.date_valid_from:
        #         currency.date_valid_until = self.date_valid_from.__str__() - datetime.timedelta(days=1)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['date_valid_from']
        indexes = [
            models.Index(fields=['currency_name', 'date_valid_from', 'date_valid_until']),
        ]
