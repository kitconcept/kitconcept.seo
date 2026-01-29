# Changelog

<!--
   You should *NOT* be adding new change log entries to this file.
   You should create a file in the news directory instead.
   For helpful instructions, please see:
   https://github.com/plone/plone.releaser/blob/master/ADD-A-NEWS-ITEM.rst
-->

<!-- towncrier release notes start -->

## 2.1.3 (2026-01-27)

### Bug fixes:

- Fix removal of pkg_resources namespace. @davisagli


## 2.1.2 (2026-01-26)

### Bug fixes:

- Add new widget for seo title and description. @iFlameing


## 2.1.1 (2025-11-04)

### New features:

- Add Spanish translations #22 [macagua] (#22)

### Internal:

- Fix metadata for the package. @ericof
- Use pkgutil instead of deprecated pkg_resources. @ericof


## 2.1.0 (2024-05-30)


### New features:

- Add Plone 6 Support. @tisto (#13)
- Set the X-Robots-Tag response header when seo_noindex is True. @sneridagh, @davisagli (#17)

### Internal:

- Update internal package structure. @sneridagh, @davisagli (#16)


## 2.0.1 (2021-11-01)

- Explicitly include dependencies (supporting pip installations)
  [ericof]

- Use **plone/setup-plone@v1.0.0** in Github actions
  [ericof]

## 2.0.0 (2021-09-24)

- Add Python 3.8/3.9 support
  [tisto]

- Drop Python 2 support.
  [tisto]

- Drop Plone 5 support.
  [tisto]

- Add Italian translations.
  [cekk]

## 1.4.0 (2020-04-08)

- Remove maxlength parameter from seo fields.
  [tisto]

## 1.3.0 (2020-03-24)

- Add Open Graph title, description and image.
  [tisto]

- Add German translation.
  [tisto]

## 1.2.1 (2020-01-16)

- Re-release 1.2.0.
  [tisto]

## 1.2.0 (2020-01-16)

- Add canonical_url option.
  [tisto]

## 1.1.0 (2020-01-10)

- Add noindex option.
  [tisto]

## 1.0.0 (2019-05-14)

- Python 3 compatibility.
  [tisto]

- Plone 5.2 compatibility.
  [tisto]

- Remove unnecessary plone.directives.form test dependency.
  [tisto]

- Use black formatter.
  [tisto]

## 1.0.0a1 (2018-07-09)

- Initial release.
  [kitconcept]
