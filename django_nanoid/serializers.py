from django.utils.translation import gettext as _
from rest_framework import fields, serializers

from . import models


class NANOIDField(fields.Field):

    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        return data


serializers.ModelSerializer.serializer_field_mapping[models.NANOIDField] = NANOIDField
