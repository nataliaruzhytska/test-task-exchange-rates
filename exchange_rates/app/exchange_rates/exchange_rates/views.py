from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from .models import Currency


def health_check(request):
    return HttpResponse('OK')


class CurrencyListView(ListView):
    model = Currency()
    queryset = Currency.objects.all()
    template_name = 'currency_list.html'
    paginate_by = 30

    def get_all(self):
        return self.queryset


class CurrencyDetailView(DetailView):
    model = Currency()
    queryset = Currency.objects.all()
    template_name = 'currency_detail.html'

    def get_currency(self):
        return self.queryset.filter(currency_id=self.kwargs.get('currency_id'))
