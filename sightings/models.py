from django.db import models
from django.utils.translation import gettext as _

class Sighting(models.Model):
    x_coord = models.FloatField(
        max_length=25,
        help_text=_('X coordinate of sighting')
    )
    y_coord = models.FloatField(
        max_length=25,
        help_text=_('Y coordinate of sighting')
    )
    squirrel_id = models.CharField(
        max_length=15,
        help_text=_('Unique Squirrel ID')
    )
    hectare = models.CharField(
        max_length=5,
    )

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

    date = models.IntegerField(
        help_text=_('Date MMDDYYYY'),
    #date = models.DateField( ?
    )
    hectare_num = models.IntegerField(
        help_text=_('Hectare Squirrel Number'),
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

    primary_fur = models.CharField(
        max_length=10,
        #choices=
        blank=True,
        help_text=_('Primary fur color'),
    )
    highlight_fur = models.CharField(
        max_length=20,
        blank=True,
        help_text=_('Highlight fur color')
    )

    running = models.BooleanField(
        help_text=_('Whether or not squirrell is running'),
    )
