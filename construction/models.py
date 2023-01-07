from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q

from construction.constants import USER_TYPE_CHOICES, POSITION_CHOICES, STATUS_CHOICES


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


class JobUser(models.Model):
    class Meta:
        db_table = 'job_user'
        verbose_name = 'Job User'
        verbose_name_plural = 'Job Users'
        unique_together = ('job', 'user')

    job = models.ForeignKey(Job, related_name='job_users', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='job_users', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        try:
            # @todo Ask if pending job is considered that the worker is engaged
            JobUser.objects.get(
                Q(job__start_date__range=(self.job.start_date, self.job.end_date)) |
                Q(job__end_date__range=(self.job.start_date, self.job.end_date)) |
                Q(job__start_date__lt=self.job.start_date, job__end_date__gt=self.job.end_date),
                user=self.user,
                job__status__in=[1, 3],
            )
            raise ValidationError('User {} is already engaged on another Job'.format(self.user))
        except JobUser.DoesNotExist:
            super(JobUser, self).save(*args, **kwargs)
