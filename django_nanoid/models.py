import nanoid
from django.db import models
from django.utils.translation import gettext as _


class NANOIDField(models.Field):

    empty_strings_allowed = False

    def __init__(self, verbose_name=None, **kwargs):
        self.editable = kwargs.pop('editable', True)
        self.secure_generated = kwargs.pop('secure_generated', True)
        self.alphabetically = kwargs.pop('alphabetically', None)
        self.size = kwargs.pop('size', None)

        if self.size and not isinstance(self.size, int):
            raise ValueError("Size parameter must be an integer.")

        if self.alphabetically and not isinstance(self.alphabetically, str):
            raise ValueError("Alphabetically parameter must be an string.")

        if self.size and not self.alphabetically:
            raise ValueError("Need to specify a alphabetically parameter")

        if self.alphabetically and not self.size:
            raise ValueError("Need to specify a size parameter")

        kwargs.setdefault('max_length', 21)
        super().__init__(verbose_name, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs['max_length']
        kwargs['secure_generated'] = self.secure_generated
        kwargs['alphabetically'] = self.alphabetically
        kwargs['size'] = self.size
        return name, path, args, kwargs

    def get_internal_type(self):
        return 'CharField'

    def generate_nanoid(self):
        if self.secure_generated:
            if self.size and self.alphabetically:
                return nanoid.generate(size=self.size, alphabet=self.alphabetically)
            else:
                return nanoid.generate()
        else:
            if self.size and self.alphabetically:
                return nanoid.non_secure_generate(size=self.size, alphabet=self.alphabetically)
            else:
                return nanoid.non_secure_generate()

    def pre_save(self, model_instance, add):
        value = getattr(model_instance, self.attname)
        if value is None and add:
            value = self.generate_nanoid()
            setattr(model_instance, self.attname, value)
        return value

    def get_prep_value(self, value):
        value = super().get_prep_value(value)
        if value is not None and self.alphabetically:
            value = str(value).lower()
        return value
