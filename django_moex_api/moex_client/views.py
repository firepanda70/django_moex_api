from dataclasses import asdict

from django.http import JsonResponse
from django.views.decorators.cache import cache_page

from django_moex_api.settings import TIMEOUT
from moex_client import moex_client, MOEXClinetException


@cache_page(TIMEOUT)
def get_current_usd(request):
    history = moex_client.get_history()
    try:
        last = moex_client.get_usd_rub_rate()
    except MOEXClinetException:
        if len(history) == 0:
            return JsonResponse({'exc': 'Temporaly unavaliable'}, status=500)
        last = history[-1]
    data = {
        'last': asdict(last),
        'history': [
            asdict(el) for el in history
        ]
    }
    return JsonResponse(data)
