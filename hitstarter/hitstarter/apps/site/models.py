from django.db import models
from django import forms 
from django.forms import ModelForm
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.template.defaultfilters import slugify
from django.conf import settings

from taggit.managers import TaggableManager
from userena.models import UserenaLanguageBaseProfile
from userena.signals import signup_complete
from datetime import datetime, timedelta
from django_thumbs.db.models import ImageWithThumbsField

import os, binascii, markdown

class Project(models.Model):
    user_owner = models.ForeignKey(User)

    public = models.BooleanField(_("Public"),
                                    default=True, 
                                    blank=True)

    featured = models.BooleanField(_("Featured"),
                                    default=False, 
                                    blank=True)

    featured_date = models.DateTimeField('Time featured', 
                                    null=True,
                                    blank=True, 
                                    default=datetime.utcnow)

    red_flagged = models.BooleanField(_("Red Flagged"),
                                    default=False, 
                                    blank=True)

    deleted = models.BooleanField(_("Deleted"),
                                    default=False, 
                                    blank=True)

    first_posted = models.DateTimeField('First Posted', 
                                    blank=True, 
                                    default=datetime.utcnow)

    last_edited = models.DateTimeField('Last Edited', 
                                    blank=True, 
                                    default=datetime.utcnow)

    ###############
    # Externals
    #   - Public facing information
    ###############

    title = models.CharField(_('Title'), 
                                    max_length=254,
                                    blank=True,
                                    null=True)  

    slug = models.SlugField(_('Slug'),
                                    blank=True,
                                    null=True)

    wallet = models.CharField(_('wallet'), 
                                    max_length=254,
                                    blank=True,
                                    null=True)  

    target = models.IntegerField()

    tags = TaggableManager()

    # Thumbnail. We might have to nuke this.
    thumbnail = ImageWithThumbsField(_('Thumbnail'), 
                                    upload_to='uploads', 
                                    sizes=((125,125),(200,200)), 
                                    blank=True, 
                                    null=True)

    description = models.TextField(_('Description'), 
                                    blank=True,
                                    null=True)

    description_mkd = models.TextField(_('Description (Markdown)'), 
                                    blank=True,
                                    null=True)

def get_project_by_id(id):
    if not id:
        return None

    try:
        return Project.objects.get(pk=id)
    except Exception, e:
        return None

def get_featured_projects():

    try:
        return Project.objects.filter(featured=True)
    except Exception, e:
        return None
