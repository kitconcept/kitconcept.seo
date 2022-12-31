# -*- coding: utf-8 -*-
from kitconcept.seo import _
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.namedfile.field import NamedBlobImage
from plone.supermodel import model
from zope import schema
from zope.component import adapter
from zope.interface import implementer
from zope.interface import provider


@provider(IFormFieldProvider)
class ISeo(model.Schema):

    model.fieldset(
        "seo",
        label=_("SEO"),
        fields=[
            "seo_title",
            "seo_description",
            "seo_noindex",
            "seo_canonical_url",
            #            "seo_nofollow",
            #            "seo_noarchive",
            #            "seo_nosnippet",
            "opengraph_title",
            "opengraph_description",
            "opengraph_image",
        ],
    )

    seo_title = schema.TextLine(
        title=_("Title"),
        description=_(
            "Override the meta title. When empty the default title will "
            + "be used. Use maximum 50 characters."
        ),
        required=False,
    )

    seo_description = schema.TextLine(
        title=_("Description"),
        description=_(
            "Override the meta description. When empty the default "
            + "description will be used. Use maximum 150 characters."
        ),
        required=False,
    )

    # https://support.google.com/webmasters/answer/93710?hl=en
    seo_noindex = schema.Bool(
        title=_("No Index"),
        description=_("Prevents a page from appearing in search engines"),
        required=False,
    )

    # https://support.google.com/webmasters/answer/139066?hl=en
    seo_canonical_url = schema.URI(
        title=_("Canonical URL"),
        description=_(
            "Tells the search engine to choose this URL as the canonical version and crawl that."
        ),
        required=False,
    )

    # # https://support.google.com/webmasters/answer/96569?hl=en
    # seo_nofollow = schema.Bool(
    #     title=_(u"No Follow"),
    #     description=_(u"Prevents search engines to follow links on this page"),
    #     required=False,
    # )

    # # https://support.google.com/webmasters/answer/79812?hl=en
    # seo_noarchive = schema.Bool(
    #     title=_(u"No Archive"),
    #     description=_(
    #         u"Prevents search engines to store a cached copy of this page"),
    #     required=False,
    # )

    # # https://support.google.com/webmasters/answer/96569?hl=en
    # seo_nosnippet = schema.Bool(
    #     title=_(u"No Snippet"),
    #     description=_(
    #         u"Prevents search engines from displaying a snippet for your page in search results"  # noqa
    #     ),
    #     required=False,
    # )

    opengraph_title = schema.TextLine(
        title=_("Open Graph Title"),
        description=_(
            "Override the Open Graph title, that Facebook and Twitter use. When empty the default title will "
            + "be used. Use maximum 60 characters."
        ),
        required=False,
    )

    opengraph_description = schema.TextLine(
        title=_("Open Graph Description"),
        description=_(
            "Override the Open Graph description, that Facebook and Twitter use. When empty the default "
            + "description will be used. Use maximum 155 characters."
        ),
        required=False,
    )

    opengraph_image = NamedBlobImage(
        title=_("Open Graph Image"),
        description=_(
            "Override the Open Graph image, that Facebook and Twitter use. When empty the default "
            + "lead image will be used. Recommended image ratio is 1,91:1 and 1200 x 630px."
        ),
        required=False,
    )


@implementer(ISeo)
@adapter(IDexterityContent)
class Seo(object):
    def __init__(self, context):
        self.context = context
