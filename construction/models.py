from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Q
from rest_framework.exceptions import ValidationError

from construction.constants import USER_TYPE_CHOICES, POSITION_CHOICES, STATUS_CHOICES, STATUS_CHOICES_DICTIONARY, \
    POSITION_CHOICES_DICTIONARY


# Create your models here.

class User(AbstractUser):
    class Meta:
        db_table = 'user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    # @todo Change choices to the real types

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    user_type = models.IntegerField(choices=USER_TYPE_CHOICES, default=1)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class ConstructionSite(models.Model):
    class Meta:
        db_table = 'construction_site'
        verbose_name = 'Construction Site'
        verbose_name_plural = 'Construction Sites'

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Trellis(models.Model):
    class Meta:
        db_table = 'trellis'
        verbose_name = 'Trellis'
        verbose_name_plural = 'Trellises'

    construction_site = models.ForeignKey(ConstructionSite, related_name='trellises', on_delete=models.CASCADE)
    number = models.PositiveIntegerField(default=1)
    base_area = models.DecimalField(max_digits=7, decimal_places=2)
    top_area = models.DecimalField(max_digits=7, decimal_places=2)
    # @todo ask why total area is needed when we can just add two areas above
    total_area = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return 'Trellis {}'.format(self.number)


class Job(models.Model):
    class Meta:
        db_table = 'job'
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'

    trellis = models.ForeignKey(Trellis, related_name='jobs', on_delete=models.CASCADE)
    position = models.IntegerField(choices=POSITION_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.IntegerField(choices=STATUS_CHOICES)

    def __str__(self):
        return '{} {} - {}'.format(self.trellis, POSITION_CHOICES_DICTIONARY[self.position],
                                   STATUS_CHOICES_DICTIONARY[self.status])


class JobUser(models.Model):
    class Meta:
        db_table = 'job_user'
        verbose_name = 'Job User'
        verbose_name_plural = 'Job Users'
        unique_together = ('job', 'user')

    job = models.ForeignKey(Job, related_name='job_users', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='job_users', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return '{} {}, from {} - to {}'.format(self.job, self.user, self.start_date, self.end_date)

    def save(self, *args, **kwargs):
        if self.start_date is None:
            self.start_date = self.job.start_date
        if self.end_date is None:
            self.end_date = self.job.end_date
        if self.job.status == 1:
            try:
                # @todo Ask if pending job is considered that the worker is engaged
                JobUser.objects.get(
                    Q(job__start_date__range=(self.job.start_date, self.job.end_date)) |
                    Q(job__end_date__range=(self.job.start_date, self.job.end_date)) |
                    Q(job__start_date__lt=self.job.start_date, job__end_date__gt=self.job.end_date),
                    user=self.user,
                    job__status__in=[1]
                )
                raise ValueError('User {} is already engaged on another Job'.format(self.user))
            except JobUser.DoesNotExist:
                super(JobUser, self).save(*args, **kwargs)
