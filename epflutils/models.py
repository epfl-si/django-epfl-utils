from django.db import models
import django.utils.translation


class LabelModel(models.Model):
    """ Model for French and english label """

    fr_label = models.CharField(
        max_length=100)

    en_label = models.CharField(
        max_length=100)

    def __unicode__(self):
        lang = django.utils.translation.get_language()
        return self.__getattribute__(lang + '_label')

    class Meta:
        abstract = True
