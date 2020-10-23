from django.db import models
from django.utils.translation import gettext as _

class Sighting(models.Model):
    longitude = models.CharField(
        #validators=[validate_comma_separated_integer_list],
        max_length=25,
        help_text=_('X coordinate of sighting')
    )

    latitude = models.CharField(
        #validators=[validate_comma_separated_integer_list],
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
        auto_now_add=True,
    )

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
        blank=True,
        help_text=_('Primary fur color'),
    )

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
        blank=True,
    )
    chasing = models.BooleanField(
        help_text=_('Whether or not squirrel is chasing'),
        blank=True,
    )

    climbing = models.BooleanField(
        help_text=_('Whether or not squirrel is climbing'),
        blank=False,
    )
    eating = models.BooleanField(
        help_text=_('Whether or not squirrel is eating'),
        blank=False,
    )
    foraging = models.BooleanField(
        help_text=_('Whether or not squirrell is foraging'),
        blank=False,
    )
    other_activities = models.TextField(
        max_length=300,
        blank=True,
    )
    tail_flags = models.BooleanField(
        help_text=_('Whether or not squirrel tail flags'),
        blank=False,
    )
    tail_twitches = models.BooleanField(
        help_text=_('Whether or not squirrel tail twitches'),
        blank=False,
    )
    approaches = models.BooleanField(
        help_text=_('Whether or not squirrel is approaching'),
        blank=False,
    )
    indifferent = models.BooleanField(
        help_text=_('Whether or not squirrel is indifferent'),
        blank=False,
    )
    runs_from = models.BooleanField(
        help_text=_('Whether or not squirrel is running from observer'),
        blank=False,
