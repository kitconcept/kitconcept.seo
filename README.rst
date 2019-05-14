.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

==============================================================================
kitconcept.seo
==============================================================================

.. image:: https://travis-ci.org/kitconcept/kitconcept.seo.svg?branch=master
    :target: https://travis-ci.org/kitconcept/kitconcept.seo

.. image:: https://img.shields.io/pypi/status/kitconcept.seo.svg
    :target: https://pypi.python.org/pypi/kitconcept.seo/
    :alt: Egg Status

.. image:: https://img.shields.io/pypi/v/kitconcept.seo.svg
    :target: https://pypi.python.org/pypi/kitconcept.seo
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/l/kitconcept.seo.svg
    :target: https://pypi.python.org/pypi/kitconcept.seo
    :alt: License

|

.. image:: https://raw.githubusercontent.com/kitconcept/kitconcept.seo/master/kitconcept.png
   :alt: kitconcept
   :target: https://kitconcept.com/

SEO enhancements for the Plone Content Management System. Please note that kitconcept.seo is an add-on product for `Volto <https://github.com/plone/volto>`_, the React-based frontend for Plone that will become Plone 6.
If you are looking for a full featured SEO solution for Plone 4, we suggest looking into `fourdigits.seo <https://pypi.org/project/fourdigits.seo/>`_.

Features
--------

- Adds SEO fieldset to Dexterity content types to override title and description for SEO


Examples
--------

This add-on can be seen in action at the following sites:

- `VHS Ehrenamtsportal <www.vhs-ehrenamtsportal.de>`_


Translations
------------

This product has been translated into

- German


Installation
------------

Install kitconcept.seo by adding it to your buildout::

    [buildout]

    ...

    eggs =
        kitconcept.seo


and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/kitconcept/kitconcept.seo/issues
- Source Code: https://github.com/kitconcept/kitconcept.seo


Support
-------

If you are having issues, please let us know: info@kitconcept.com.


License
-------

The project is licensed under the GPLv2.
