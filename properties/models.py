# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django_extensions.db.models import TimeStampedModel
from django.db import models

from authentication.models import User

import constants
# Create your models here.


class Picture(TimeStampedModel):
    image = models.ImageField(blank=True)

    def __str__(self):
        return "Picture Number {}".format(self.pk)


class Room(TimeStampedModel):
    images = models.ManyToManyField(Picture, blank=True)
    price = models.PositiveIntegerField()
    accomodation = models.CharField(
        max_length=20,
        choices=constants.ACCOMODATIONS,
        default=constants.SINGLE,
    )
    likes = models.ManyToManyField(
        User,
        verbose_name="likes",
        blank=True,
    )
    own_kitchen = models.BooleanField(
        default=False,
        verbose_name="has own kitchen"
    )
    own_bathroom = models.BooleanField(
        default=False,
        verbose_name="has own bathroom"
    )

    def __str__(self):
        return "Room Number {}".format(self.pk)


class Property(TimeStampedModel):
    landlord = models.ForeignKey(User, related_name="property")
    rooms = models.ManyToManyField(Room, related_name="property", blank=True)
    images = models.ManyToManyField(Picture, blank=True)
    lat = models.PositiveIntegerField(null=True, blank=True)
    lng = models.PositiveIntegerField(null=True, blank=True)
    telephone_number = models.CharField(
        max_length=255,
        default='',
        blank=True
    )
    address_line_1 = models.CharField(
        max_length=255,
        default='',
        blank=True
    )
    address_line_2 = models.CharField(
        max_length=255,
        default='',
        blank=True
    )

    class Meta:
        verbose_name = "Property"

    def __str__(self):
        return "Property Number {}".format(self.pk)
