=============================
{{ cookiecutter.project_name }}
=============================

.. image:: https://badge.fury.io/py/{{ cookiecutter.repo_name }}.svg
    :target: https://badge.fury.io/py/{{ cookiecutter.repo_name }}

.. image:: https://circleci.com/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.svg?branch=master
    :target: https://circleci.com/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}

.. image:: https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}

{{ cookiecutter.project_short_description}}

Documentation
-------------

The full documentation is at https://{{ cookiecutter.repo_name }}.readthedocs.io.

Quickstart
----------

Install {{ cookiecutter.project_name }}::

    pip install {{ cookiecutter.repo_name }}

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        '{{ cookiecutter.app_name }}.apps.{{ cookiecutter.app_config_name }}',
        ...
    )

Add {{ cookiecutter.project_name }}'s URL patterns:

.. code-block:: python

    from {{ cookiecutter.app_name }} import urls as {{ cookiecutter.app_name }}_urls


    urlpatterns = [
        ...
        url(r'^', include({{ cookiecutter.app_name }}_urls)),
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
    
Register on snapPyPI
~~~~~~~~~~~~~~~~

Once you've got at least a prototype working and tests running, it's time to register the app on snapPyPI::

    python setup.py register


Releasing on snapPyPI
~~~~~~~~~~~~~~~~~

Time to release a new version? Easy!

First, use `bumpversion` to up the release number::

    $ pip install bumpversion
    $ bumpversion --current-version VERSION_NUMBER minor --config-file setup.cfg

Where `VERSION_NUMBER` is the current version, e.g. `0.1.0`.

Then run::

    $ python setup.py publish

It will answer with something like::

    You probably want to also tag the version now:
          git tag -a 0.1.0 -m 'version 0.1.0'
          git push --tags

Go ahead and follow those instructions.
Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
