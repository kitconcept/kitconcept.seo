# kitconcept.seo

[![Pypi](https://img.shields.io/pypi/status/kitconcept.seo.svg)](https://pypi.python.org/pypi/kitconcept.seo/)
[![Pypi version](https://img.shields.io/pypi/v/kitconcept.seo.svg)](https://pypi.python.org/pypi/kitconcept.seo/)
[![License](https://img.shields.io/pypi/l/kitconcept.seo.svg)](https://pypi.python.org/pypi/kitconcept.seo/)

[![kitconcept, GmbH](https://raw.githubusercontent.com/kitconcept/kitconcept.seo/master/kitconcept.png)](https://kitconcept.com/)

SEO enhancements for the Plone Content Management System.
kitconcept.seo works with the latest Plone 6 and its default frontend [Volto](https://github.com/plone/volto).
It might still work with Plone Classic but that is not officially supported.
If you are looking for a full featured SEO solution for Plone Classic or older versions of Plone, we suggest looking into [fourdigits.seo](https://pypi.org/project/fourdigits.seo/).


## Features

- Allows to override meta title and meta description per page
- Allows to set the noindex header to exclude pages from being indexed
- Allows to set a canonical URL
- Allows to set Open Graph title, description and image

## Examples

This add-on can be seen in action at the following sites:

- [German Aerospace Center (DLR)](www.dlr.de)
- [FZ Jülich](www.fz-juelich.de)
- [HI Ern](www.hi-ern.de/de)
- [Zeelandia](www.zeelandia.de)
- [VHS Ehrenamtsportal](www.vhs-ehrenamtsportal.de)

## Translations

This product has been translated into

- German

## Installation

Install kitconcept.seo with `pip`:

```shell
pip install kitconcept.seo
```
And to create the Plone site:

```shell
make create_site
```

# Enable the SEO behavior

To enable the SEO tab for a specific content type you have to enable the kitconcept.seo behavior.
Go to the page setup and then to the Dexterity Content Types control panel.
Choose the content type you want to enable SEO for and enable the `kitconcept.seo` behavior.

## Enable the SEO behavior programmatically

Enable the kitconcept.seo behavior by adding the behavior to the Factory Type Information (FTI) of your type in your generic setup profile. E.g. to enable SEO for the document type, drop a Document.xml file into the `profiles/default/types` folder of your add-on product with the following content:

```xml
   <?xml version="1.0" encoding="utf-8"?>
   <object name="Document" meta_type="Dexterity FTI" i18n:domain="plone"
     xmlns:i18n="http://xml.zope.org/namespaces/i18n">
     <property name="behaviors" purge="False">
       <element value="kitconcept.seo" />
     </property>
   </object>
```

## Add to Volto project or add-on

To add `kitconcept.seo` to your Volto project/add-on you need to edit the component you want to use it for.
If you want use it for your whole page you can use it in the ``View.jsx`` (see [here](https://6.docs.plone.org/volto/development/customizing-views.html) for further information on editing views in Volto).

Than you use `react-helmet` Volto helper to set the title and description of the component. So import `react-helmet`
with:

```jsx
   import { Helmet } from '@plone/volto/helpers';
```

And finally add this to the `jsx` code of your component:

```jsx
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
```

## Usage

In your Volto page you need to go to the edit mode of the page you want to add a title and description for SEO and open the properties of the page by clicking the properties under the save button. Choose SEO there and add a title and description in the fields. When you are done hit the save button.

## Contribute

- [Issue Tracker](https://github.com/collective/kitconcept.seo/issues)
- [Source Code](https://github.com/collective/kitconcept.seo/)

## License

The project is licensed under GPLv2.
