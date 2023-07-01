# django-nanoid
[A tiny, secure, URL-friendly, unique string ID generator for Python.](https://github.com/puyuan/py-nanoid) support in [Django](https://www.djangoproject.com/).

[![PyPI Version](https://badge.fury.io/py/django-nanoid.svg)](https://badge.fury.io/py/django-nanoid)
[![PyPI Versions](https://img.shields.io/pypi/pyversions/django-nanoid.svg)](https://pypi.python.org/pypi/django-nanoid)

### Status

This project is actively maintained.

### Installation

To install django-nanoid from [pip](https://pypi.python.org/pypi/pip):
```bash
    $ pip install django-nanoid
```

To install nanoid from source:
```bash
    $ git clone git@github.com:yosephbernandus/django-nanoid.git
    $ cd django-nanoid && python setup.py install
```

### Usage

Adding a NANOID field to your Django models is straightforward, default length is 21. Can adjust the length using max_length

```python
from django.db import models
from django_nanoid.models import NANOIDField

class Post(models.Model):
    id = NANOIDField(secure_generated=True, editable=False)
```

Passing this will automatically generate a unique identifier, with secure generated

```python
from django.db import models
from django_nanoid.models import NANOIDField

class Post(models.Model):
    post_identifier = NANOIDField(size=10, alphabetically='mnhjksloiwnhA..!@$$$!#', secure_generated=False)
```

Passing this will automatically generate a unique identifier, with non_secure_generated with custom alphabetically and length

### Contributing

If you would like to contribute, simply fork the repository, push your changes and send a pull request.
Pull requests will be brought into the `master` branch via a rebase and fast-forward merge with the goal of having a linear branch history with no merge commits.

### License

[Apache 2.0](LICENSE)

### Dependencies

* [Django](https://github.com/django/django)
* [py-nanoid](https://github.com/puyuan/py-nanoid.git)
