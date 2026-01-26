"""Installer for the kitconcept.seo package."""

from pathlib import Path
from setuptools import find_namespace_packages
from setuptools import setup


long_description = f"""
{Path("README.md").read_text()}\n
{Path("CONTRIBUTORS.md").read_text()}\n
{Path("CHANGES.md").read_text()}\n
"""


setup(
    name="kitconcept.seo",
    version="2.1.2",
    description="SEO optimizations plugin for Plone",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 6.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    keywords="Python Plone CMS",
    author="kitconcept GmbH",
    author_email="info@kitconcept.com",
    url="https://pypi.python.org/pypi/kitconcept.seo",
    project_urls={
        "PyPI": "https://pypi.python.org/pypi/kitconcept.seo",
        "Source": "https://github.com/kitconcept/kitconcept.seo",
        "Tracker": "https://github.com/kitconcept/kitconcept.seo/issues",
    },
    license="GPL version 2",
    packages=find_namespace_packages(where="src/", include=["kitconcept.*"]),
    namespace_packages=["kitconcept"],
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.8",
    install_requires=[
        "setuptools",
        "Products.CMFPlone",
        "plone.app.dexterity",
        "plone.autoform",
        "plone.behavior",
        "plone.dexterity",
        "plone.namedfile",
        "plone.supermodel",
    ],
    extras_require={
        "test": [
            "zest.releaser[recommended]",
            "zestreleaser.towncrier",
            "plone.app.contenttypes[test]",
            "plone.app.testing",
            "plone.restapi[test]",
            # Undeclared dependency of plone.restapi,
            # can be removed after next release
            "plone.app.iterate",
            "pytest",
            "pytest-cov",
            "pytest-plone>=0.2.0",
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    [console_scripts]
    update_dist_locale = kitconcept.seo.locales.update:update_locale
    """,
)
