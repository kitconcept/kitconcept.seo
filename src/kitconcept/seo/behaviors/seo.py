# -*- coding: utf-8 -*-
from kitconcept.seo import _
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope import schema
from zope.component import adapter
from zope.interface import implementer
from zope.interface import provider


@provider(IFormFieldProvider)
class ISeo(model.Schema):

    model.fieldset(
        "seo",
        label=_(u"SEO"),
        fields=[
            "seo_title",
            "seo_description",
            "seo_noindex",
            "seo_nofollow",
            "seo_noarchive",
            "seo_nosnippet",
        ],
    )

    seo_title = schema.TextLine(
        title=_("Title"),
        description=_(
            u"Override the meta title. When empty the default title will "
            + u"be used. Use maximum 50 chararcters."
        ),
        required=False,
        max_length=70,
    )

    seo_description = schema.TextLine(
        title=_(u"Description"),
        description=_(
            u"Override the meta description. When empty the default "
            + u"description will be used. Use maximum 150 characters."
        ),
        required=False,
        max_length=155,
    )

    # https://support.google.com/webmasters/answer/93710?hl=en
    seo_noindex = schema.Bool(
        title=_(u"No Index"),
        description=_(u"Prevents a page from appearing in search engines"),
        required=False,
    )

    # https://support.google.com/webmasters/answer/96569?hl=en
    seo_nofollow = schema.Bool(
        title=_(u"No Follow"),
        description=_(u"Prevents search engines to follow links on this page"),
        required=False,
    )

    # https://support.google.com/webmasters/answer/79812?hl=en
    seo_noarchive = schema.Bool(
        title=_(u"No Archive"),
        description=_(u"Prevents search engines to store a cached copy of this page"),
        required=False,
    )

    # https://support.google.com/webmasters/answer/96569?hl=en
    seo_nosnippet = schema.Bool(
        title=_(u"No Snippet"),
        description=_(
            u"Prevents search engines from displaying a snippet for your page in search results"
        ),
        required=False,
    )


@implementer(ISeo)
@adapter(IDexterityContent)
class Seo(object):
    def __init__(self, context):
        self.context = context
