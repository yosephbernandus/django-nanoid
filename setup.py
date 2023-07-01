import ast
import re
from setuptools import setup

version_regex = re.compile(r'__version__\s+=\s+(.*)')


def get_version():
    with open('django_nanoid/__init__.py', 'r') as f:
        return str(ast.literal_eval(version_regex.search(f.read()).group(1)))


setup(
    name='django-nanoid',
    version=get_version(),
    author='Yoseph Bernandus',
    author_email='yosephbernandus@gmail.com',
    packages=['django_nanoid'],
    url='https://github.com/yosephbernandus/django-nanoid',
    license='Apache 2.0',
    description='Universally Unique Lexicographically Sortable Identifier (ULID) support in Django',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    package_data={'': ['README.md']},
    install_requires=['django>=1.9', 'nanoid', 'djangorestframework>=3.0.0'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)