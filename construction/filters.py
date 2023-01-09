from datetime import datetime

from django.db.models import Q
from django_filters import rest_framework as filters
from django_filters.widgets import RangeWidget

from construction.constants import BUSY_OR_FREE_CHOICES, POSITION_CHOICES
from construction.models import User, Job, ConstructionSite, Trellis, JobUser


class UserFilter(filters.FilterSet):
    not_busy = filters.ChoiceFilter(label='Busy or Free', method='filter_busy_or_not', choices=BUSY_OR_FREE_CHOICES)
    position = filters.ChoiceFilter(
        field_name="job_users__job__position", choices=POSITION_CHOICES,
        label="Job position")
    no_experience = filters.BooleanFilter(
        field_name="job_users", lookup_expr='isnull', label="Not worked before")
    work_date_range = filters.DateFromToRangeFilter(
        label='Work Date Range', method="filter_by_range",
        widget=RangeWidget(attrs={'class': 'datepicker', 'type': 'date'})
    )

    class Meta:
        model = User
        fields = ['user_type']

    def filter_by_range(self, queryset, name, value):
        return queryset.filter(
            Q(job_users__start_date__range=(value.start.date(), value.stop.date()))
            |
            Q(job_users__end_date__range=(value.start.date(), value.stop.date()))
            |
            Q(job_users__start_date__lt=value.start.date(), job_users__end_date__gt=value.stop.date()),
            job_users__job__status__in=[1],
        )

    def filter_busy_or_not(self, queryset, name, value):
        """

         sqlite3 does not support .distinct("job_users__user_id")

        """
        busy_user_ids = Job.objects.filter(
            status__in=[1],
            job_users__start_date__lte=datetime.now().date(),
            job_users__end_date__gte=datetime.now().date()
        ).values_list("job_users__user_id", flat=True)
        if value == "Busy":
            return queryset.filter(id__in=busy_user_ids)
        else:
            return queryset.exclude(id__in=busy_user_ids)


class ConstructionSiteFilter(filters.FilterSet):
    class Meta:
        model = ConstructionSite
        fields = ['name']


class TrellisFilter(filters.FilterSet):
    class Meta:
        model = Trellis
        fields = ['construction_site', 'number', 'base_area', 'top_area', 'total_area']


class JobFilter(filters.FilterSet):
    class Meta:
        model = Job
        fields = ['trellis', 'position', 'start_date', 'end_date']


class JobUserFilter(filters.FilterSet):
    class Meta:
        model = JobUser
        fields = ['job', 'user', 'start_date', 'end_date']
