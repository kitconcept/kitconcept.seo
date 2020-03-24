.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

kitconcept.seo
==============

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

- Allows to override meta title and meta description per page
- Allows to set the noindex header to exclude pages from being indexed
- Allows to set a canonical URL
- Allows to set Open Graph title, description and image

.. image:: https://raw.githubusercontent.com/kitconcept/kitconcept.seo/master/kitconcept-seo.png
   :alt: kitconcept

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

Than start up your Plone site and open it on ``localhost:8080`` in your browser. Log into your site and
and click on the user symbol on the bottom left of the page. Choose Site Setup there.
Now go to Add-ons and click Install at kitconcept.seo.

Enable the SEO behavior
^^^^^^^^^^^^^^^^^^^^^^^

To enable the SEO tab for a specific content type you have to enable the kitconcept.seo behavior.
Go to the page setup and then to the Dexterity Content Types control panel.
Choose the content type you want to enable SEO for and enable the `kitconcept.seo` behavior.

Enable the SEO behavior programmatically
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Enable the kitconcept.seo behavior by adding the behavior to the Factory Type Information (FTI) of your type in your generic setup profile. E.g. to enable SEO for the document type, drop a Document.xml file into the `profiles/default/types` folder of your add-on product with the following content::

   <?xml version="1.0" encoding="utf-8"?>
   <object name="Document" meta_type="Dexterity FTI" i18n:domain="plone"
     xmlns:i18n="http://xml.zope.org/namespaces/i18n">
     <property name="behaviors" purge="False">
       <element value="kitconcept.seo" />
     </property>
   </object>


Add to Volto site
-----------------

To add kitconcept.seo to your Volto page you need to edit the component you want to use it for.
If you want use it for your whole page you can use it in the ``View.jsx`` (see `here <https://docs.voltocms.com/05-customizing/04-customizing-views/>`_ for further information on editing views in Volto).
First you have to define the PropTypes for the seo elements by adding::

   seo_title: PropTypes.string,
   seo_description: PropTypes.string,

... to the PropTypes of the component.

Than you use React-Helmet to set the title and description of the component. So import React-Helmet
with::

   import Helmet from 'react-helmet';


And finally add this to the jsx code of your component::

   <Helmet
          title={
            this.props.content.seo_title
              ? this.props.content.seo_title
              : this.props.content.title
          }
          meta={
            this.props.content.seo_description
              ? [
                  {
                    name: 'description',
                    content: this.props.content.seo_description,
                  },
                ]
              : [
                  {
                    name: 'description',
                    content: this.props.content.description,
                  },
                ]
          }
          bodyAttributes={{
            class: `view-${viewName.toLowerCase()}`,
          }}
        />


Usage in Volto
--------------
In your Volto page you need to go to the edit mode of the page you want to add a title and description for SEO and open the properties of the page by clicking the properties under the save button. Choose SEO there and add a title and description in the fields. When you are done hit the save button.


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
