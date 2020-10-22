from django.db import models
from django.utils.translation import gettext as _

class Sighting(models.Model):
    longitude = models.FloatField(
        max_length=25,
        help_text=_('X coordinate of sighting')
    )

    latitude = models.FloatField(
        max_length=25,
        help_text=_('Y coordinate of sighting')
    )
    unique_squirrel_id = models.CharField(
        max_length=15,
        help_text=_('Unique Squirrel ID')
    )
    #hectare = models.CharField(
    #    max_length=5,
    #)

    AM = 'AM'
    PM = 'PM'
    SHIFTS = [
        (AM, _('AM')),
        (PM, _('PM')),
    ]
    shift = models.CharField(
        max_length=5,
        choices=SHIFTS,
    )

    #date = models.IntegerField(
    #    help_text=_('Date MMDDYYYY'),
    date = models.DateField(
        auto_now=False,
    )

    #hectare_num = models.IntegerField(
    #    help_text=_('Hectare Squirrel Number'),
    #)

    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
    AGES = [
        (ADULT, _('Adult')),
        (JUVENILE, _('Juvenile')),
    ]
    age = models.CharField(
        max_length=10,
        choices=AGES,
        blank=True,
    )

    primary_fur_color = models.CharField(
        max_length=10,
        #choices=
        blank=True,
        help_text=_('Primary fur color'),
    )
    #highlight_fur = models.CharField(
    #    max_length=20,
    #    blank=True,
    #    help_text=_('Highlight fur color')
    #)

    location = models.CharField(
        max_length = 50,
        help_text =_('the location of where the squirrel was when first sighted'),
    )

    specific_location = models.CharField(
        max_length = 50,
        help_text =_('the specific location of the squirrel'),
    )

    running = models.BooleanField(
        help_text=_('Whether or not squirrel is running'),
    )

    chasing = models.BooleanField(
        help_text=_('Whether or not squirrel is chasing'),
    )

    climbing = models.BooleanField(
        help_text=_('Whether or not squirrel is climbing'),
    )

    eating = models.BooleanField(
        help_text=_('Whether or not squirrel is eating'),
    )

    foraging = models.BooleanField(
        help_text=_('Whether or not squirrell is foraging'),
    )

    other_activities = models.TextField(
        max_length=300,
        blank=True,
    )

    kuks = models.BooleanField(
        help_text=_('Whether or not squirrel kuks'),
    )

    quaas = models.BooleanField(
        help_text=_('Whether or not squirrel quaas'),
    )

    moans = models.BooleanField(
        help_text=_('Whether or not squirrel moans'),
    )

    tail_flags = models.BooleanField(
        help_text=_('Whether or not squirrel tail flags'),
    )

    tail_twitches = models.BooleanField(
        help_text=_('Whether or not squirrel tail twitches'),
    )

    approaches = models.BooleanField(
        help_text=_('Whether or not squirrel is approaching'),
    )

    indifferent = models.BooleanField(
        help_text=_('Whether or not squirrel is indifferent'),
    )

    runs_from = models.BooleanField(
        help_text=_('Whether or not squirrel is running from observer'),
    )
