from django_filters import rest_framework as filters

from construction.constants import STATUS_CHOICES, BUSY_OR_FREE_CHOICES, POSITION_CHOICES
from construction.models import User


class UserFilter(filters.FilterSet):
    not_busy = filters.ChoiceFilter(label='Busy or Free', method='filter_busy_or_not', choices=BUSY_OR_FREE_CHOICES)
    position = filters.ChoiceFilter(
        field_name="job_users__job__position", choices=POSITION_CHOICES,
        label="Job position")
    no_experience = filters.BooleanFilter(
        field_name="job_users", lookup_expr='isnull', label="Not worked before")
    worked_from_field = filters.DateFilter(label='Worked From', method='worked_from')
    worked_to_field = filters.DateFilter(label='Worked To', method='worked_to')

    # work_date_range = filters.DateFromToRangeFilter(label='Date Range')

    class Meta:
        model = User
        fields = ['user_type']

    def filter_busy_or_not(self, queryset, name, value):
        # @todo add date check also
        if value == "Busy":
            return queryset.filter(job_users__job__status__in=[1, 3]).distinct()
        else:
            return queryset.filter(
                job_users__job__status__in=[2, 4]
            ).exclude(job_users__job__status__in=[1, 3]).distinct()

    def worked_from(self, queryset, name, value):
        # @todo needed filters
        return queryset

    def worked_to(self, queryset, name, value):
        # @todo needed filters
        return queryset
