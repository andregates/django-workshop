from django.shortcuts import render
from workshop.models import EventParticipant, Image, Interest
from django.core import serializers
from django.http import JsonResponse
from django.db.models import F, Count, Avg, Window, ExpressionWrapper, FloatField


def home_page(request):
    """Render the Dashboard od application"""
    return render(request, f'dashboard.html')


def get_dashboard_partials(request):
    """Get all dashboards updated data."""
    participants = EventParticipant.objects.all()
    participants_all = participants.count()
    participants_join = participants.filter(join=True).count()
    participants_external = participants_all - participants_join
    participants_list = list(participants.annotate(
        img=F('image__image')).values(
        "img", "name", "company").order_by("name"))

    knowledge_labels = []
    knowledge_series = []
    knowledge_results = (
        participants.values('knowledge_level').distinct().annotate(
            level_total=Window(
                expression=Count('id'),
                partition_by=[F('knowledge_level')],)).annotate(
                    percentage=ExpressionWrapper(
                        F('level_total') * 100.0 / participants_all,
                        output_field=FloatField())).values(
                            'knowledge_level',
                            'percentage')
                        )

    for result in knowledge_results:
        knowledge_labels.append(result['knowledge_level'])
        knowledge_series.append(float("{:.2f}".format(result['percentage'])))

    knowledge_chart = {
        "series": knowledge_series,
        "labels": knowledge_labels
    }

    interests = EventParticipant.interests.through.objects.all()
    interest_count = interests.count()
    interest_labels = []
    interest_series = []
    interest_results = (
        interests.values('interest__description').distinct().annotate(
            level_total=Window(
                expression=Count('id'),
                partition_by=[F('interest__description')], )).annotate(
            percentage=ExpressionWrapper(
                F('level_total') * 100.0 / interest_count,
                output_field=FloatField())).values(
            'interest__description',
            'percentage')
    )

    for result in interest_results:
        interest_labels.append(result['interest__description'])
        interest_series.append(float("{:.2f}".format(result['percentage'])))

    interest_chart = {
        "series": interest_series,
        "labels": interest_labels
    }

    others_interest = list(participants.filter(other_interest__isnull=False).values_list(
        'other_interest', flat=True))

    partials = {
        "all_part": participants_all,
        "part_join": participants_join,
        "part_ext": participants_external,
        "list": participants_list,
        "knowledge_chart": knowledge_chart,
        "interest_chart": interest_chart,
        "other_interest": others_interest
    }

    return JsonResponse(partials, safe=False)


