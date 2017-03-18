from django.db import models
from epflutils.models import LabelModel


class NoAbstractLabelModel(LabelModel):

    name = models.CharField(max_length=255)
