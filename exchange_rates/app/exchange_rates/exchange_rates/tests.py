import datetime
from django.test import TestCase
from exchange_rates.models import Currency
from exchange_rates.settings import FIXTURES


class CurrencyTest(TestCase):
    fixtures = FIXTURES

    def test_currency_add_rate(self):
        queryset = Currency.objects.filter(currency_name='USD')
        obj_count = Currency.objects.all().count()
        test_currency = Currency(currency_name='USD', purchase_rate=24.3, sale_rate=24.55,
                                 date_valid_from=datetime.date(2020, 2, 15),
                                 date_valid_until=datetime.date(2020, 2, 17))
        test_currency.save()
        currency = queryset.get(date_valid_from='2020-02-15')
        self.assertEqual(Currency.objects.all().count(), obj_count + 1)
        self.assertEqual(test_currency.date_valid_until, currency.date_valid_until)

    def test_currency_insert_rate(self):
        queryset = Currency.objects.filter(currency_name='USD')
        obj_count = Currency.objects.all().count()
        test_currency = Currency(currency_name='USD', purchase_rate=24.75, sale_rate=25.15,
                                 date_valid_from=datetime.date(2020, 1, 10),
                                 date_valid_until=datetime.date(2020, 1, 14))
        test_currency.save()
        currency = queryset.filter(date_valid_from__lt=test_currency.date_valid_from).last()
        self.assertEqual(Currency.objects.all().count(), obj_count + 1)
        self.assertEqual(currency.date_valid_until, datetime.date(2020, 1, 9))

    def test_currency_delete(self):
        queryset = Currency.objects.order_by('date_valid_from').filter(currency_name='USD')
        obj_count = Currency.objects.all().count()
        test_currency = queryset.get(date_valid_until=datetime.date(2020, 1, 14))
        test_currency.delete()
        currency = queryset.filter(date_valid_from__lt=test_currency.date_valid_from).last()
        self.assertEqual(Currency.objects.all().count(), obj_count - 1)
        self.assertEqual(currency.date_valid_until, test_currency.date_valid_until)
