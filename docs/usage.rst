=====
Usage
=====

To use django_renderblock in a project, add it to your `INSTALLED_APPS`:

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
