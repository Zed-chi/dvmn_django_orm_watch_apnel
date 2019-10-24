from datacenter.models import Visit
from django.shortcuts import render


def format_duration(duration):
    hours, remainder = divmod(duration.total_seconds(), 3600)
    minutes, seconds = divmod(remainder, 60)
    return "%02d : %02d : %02d" % (int(hours), int(minutes), int(seconds))


def storage_information_view(request):
    no_leaved = Visit.objects.filter(leaved_at=None)
    non_closed_visits = [
        {
            "who_entered": a.passcard.owner_name,
            "entered_at": a.entered_at,
            "duration": format_duration(a.get_duration()),
            "is_strange": a.is_strange(),
        } for a in no_leaved
    ]
    context = {"non_closed_visits": non_closed_visits}
    return render(request, "storage_information.html", context)
