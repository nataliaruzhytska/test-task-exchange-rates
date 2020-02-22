from django.http import HttpResponse
from django.views.generic import ListView


from .models import Currency


def health_check(request):
    return HttpResponse('OK')


class CurrencyListView(ListView):
    model = Currency()
    queryset = Currency.objects.all().order_by('currency_name', '-date_valid_from').distinct('currency_name')
    template_name = 'currency_list.html'
    paginate_by = 30

    def get_all(self):
        return self.queryset.all()


class CurrencyDetailView(ListView):
    model = Currency()

    template_name = 'currency_detail.html'
    paginate_by = 30

    def get_queryset(self):
        currency = Currency.objects.get(id=self.kwargs.get('id'))
        return Currency.objects.filter(currency_name=currency.currency_name).order_by('-date_valid_from')

