=============================
django_renderblock
=============================

.. image:: https://badge.fury.io/py/django_renderblock.svg
    :target: https://badge.fury.io/py/django_renderblock

.. image:: https://travis-ci.org/LucasGrugru/django_renderblock.svg?branch=master
    :target: https://travis-ci.org/LucasGrugru/django_renderblock

.. image:: https://codecov.io/gh/LucasGrugru/django_renderblock/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/LucasGrugru/django_renderblock

Render block in variable and use it directly in template

Documentation
-------------

The full documentation is at https://django_renderblock.readthedocs.io.

Quickstart
----------

Install django_renderblock::

    pip install django_renderblock

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_renderblock.apps.DjangoRenderblockConfig',
        ...
    )

Add django_renderblock's URL patterns:

.. code-block:: python

    from django_renderblock import urls as django_renderblock_urls


    urlpatterns = [
        ...
        url(r'^', include(django_renderblock_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox


Development commands
---------------------

::

    pip install -r requirements_dev.txt
    invoke -l


Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
