from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    context = {"passcard": passcard, "this_passcard_visits": visits}
    return render(request, "passcard_info.html", context)
