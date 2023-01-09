# Generated by Django 4.1.5 on 2023-01-07 01:55

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('user_type', models.IntegerField(choices=[(1, 'Type 1'), (2, 'Type 2'), (3, 'Type 3')], default=1)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'db_table': 'user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ConstructionSite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Construction Site',
                'verbose_name_plural': 'Construction Sites',
                'db_table': 'construction_site',
            },
        ),
        migrations.CreateModel(
            name='Trellis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(default=1)),
                ('base_area', models.DecimalField(decimal_places=2, max_digits=7)),
                ('top_area', models.DecimalField(decimal_places=2, max_digits=7)),
                ('total_area', models.DecimalField(decimal_places=2, max_digits=7)),
                ('construction_site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trellises', to='construction.constructionsite')),
            ],
            options={
                'verbose_name': 'Trellis',
                'verbose_name_plural': 'Trellises',
                'db_table': 'trellis',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(choices=[(1, 'Base'), (2, 'Top')])),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('status', models.IntegerField(choices=[(1, 'Active'), (2, 'Cancelled'), (3, 'Pending'), (4, 'Finished')])),
                ('trellis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='construction.trellis')),
            ],
            options={
                'verbose_name': 'Job',
                'verbose_name_plural': 'Jobs',
                'db_table': 'job',
            },
        ),
        migrations.CreateModel(
            name='JobUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_users', to='construction.job')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_users', to=settings.AUTH_USER_MODEL)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
            options={
                'verbose_name': 'Job User',
                'verbose_name_plural': 'Job Users',
                'db_table': 'job_user',
                'unique_together': {('job', 'user')},
            },
        ),
    ]
