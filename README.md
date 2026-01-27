# kitconcept.seo

SEO addon for Plone

[![PyPI](https://img.shields.io/pypi/v/kitconcept.seo)](https://pypi.org/project/kitconcept.seo/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/kitconcept.seo)](https://pypi.org/project/kitconcept.seo/)
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/kitconcept.seo)](https://pypi.org/project/kitconcept.seo/)
[![PyPI - License](https://img.shields.io/pypi/l/kitconcept.seo)](https://pypi.org/project/kitconcept.seo/)
[![PyPI - Status](https://img.shields.io/pypi/status/kitconcept.seo)](https://pypi.org/project/kitconcept.seo/)


[![PyPI - Plone Versions](https://img.shields.io/pypi/frameworkversions/plone/kitconcept.seo)](https://pypi.org/project/kitconcept.seo/)

[![CI](https://github.com/kitconcept/kitconcept.seo/actions/workflows/main.yml/badge.svg)](https://github.com/kitconcept/kitconcept.seo/actions/workflows/main.yml)

[![kitconcept, GmbH](https://raw.githubusercontent.com/kitconcept/kitconcept.seo/master/kitconcept.png)](https://kitconcept.com/)

[SEO](https://en.wikipedia.org/wiki/Search_engine_optimization) enhancements for the Plone Content Management System.
`kitconcept.seo` works with the latest Plone 6 and its default frontend [Volto](https://github.com/plone/volto).
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
- Italian
- Spanish

## Installation

Install kitconcept.seo with `pip`:

```shell
pip install kitconcept.seo
```

And to create the Plone site:

```shell
make create-site
```
# Enable the SEO behavior

To enable the SEO tab for a specific content type you have to enable the `kitconcept.seo` behavior.
Go to the page setup and then to the Dexterity Content Types control panel.
Choose the content type you want to enable SEO for and enable the `kitconcept.seo` behavior.

## Enable the SEO behavior programmatically

Enable the `kitconcept.seo` behavior by adding the behavior to the Factory Type Information (FTI) of your type in your generic setup profile. E.g. to enable SEO for the document type, drop a `Document.xml` file into the `profiles/default/types` folder of your add-on product with the following content:

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

- [Issue tracker](https://github.com/kitconcept/kitconcept.seo/issues)
- [Source code](https://github.com/kitconcept/kitconcept.seo/)

### Prerequisites ✅

-   An [operating system](https://6.docs.plone.org/install/create-project-cookieplone.html#prerequisites-for-installation) that runs all the requirements mentioned.
-   [uv](https://6.docs.plone.org/install/create-project-cookieplone.html#uv)
-   [Make](https://6.docs.plone.org/install/create-project-cookieplone.html#make)
-   [Git](https://6.docs.plone.org/install/create-project-cookieplone.html#git)
-   [Docker](https://docs.docker.com/get-started/get-docker/) (optional)

### Installation 🔧

1.  Clone this repository, then change your working directory.

    ```shell
    git clone git@github.com:kitconcept/kitconcept.seo.git
    cd kitconcept.seo
    ```

2.  Install this code base.

    ```shell
    make install
    ```

## License

The project is licensed under GPLv2.

## Credits and acknowledgements 🙏

Generated using [Cookieplone (0.9.10)](https://github.com/plone/cookieplone) and [cookieplone-templates (dd13073)](https://github.com/plone/cookieplone-templates/commit/dd13073d34447056d6992461d8da29447d62c029) on 2026-01-27 09:51:10.480177. A special thanks to all contributors and supporters!
