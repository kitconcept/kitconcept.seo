from kitconcept.seo import _
from plone.autoform import directives
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
            "opengraph_title",
            "opengraph_description",
            "opengraph_image",
        ],
    )

    directives.widget(
        "seo_title",
        frontendOptions={
            "widget": "softTextWidget",
            "widgetProps": {"softMaxLength": "55"},
        },
    )

    seo_title = schema.TextLine(
        title=_("Title"),
        description=_(
            "Override the meta title. When empty the default title will "
            + "be used. Use maximum 55 characters."
        ),
        required=False,
    )

    directives.widget(
        "seo_description",
        frontendOptions={
            "widget": "softTextareaWidget",
            "widgetProps": {"softMaxLength": "155"},
        },
    )

    seo_description = schema.TextLine(
        title=_("Description"),
        description=_(
            "Override the meta description. When empty the default "
            + "description will be used. Use maximum 155 characters."
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
            "Tells the search engine to choose this URL as the canonical "
            "version and crawl that."
        ),
        required=False,
    )

    opengraph_title = schema.TextLine(
        title=_("Open Graph Title"),
        description=_(
            "Override the Open Graph title, that Facebook and Twitter use. When empty "
            "the default title will be used. Use maximum 60 characters."
        ),
        required=False,
    )

    opengraph_description = schema.TextLine(
        title=_("Open Graph Description"),
        description=_(
            "Override the Open Graph description, that Facebook and Twitter use. "
            "When empty the default description will be used. "
            "Use maximum 155 characters."
        ),
        required=False,
    )

    opengraph_image = NamedBlobImage(
        title=_("Open Graph Image"),
        description=_(
            "Override the Open Graph image, that Facebook and Twitter use. "
            "When empty the default lead image will be used. Recommended image "
            "ratio is 1,91:1 and 1200 x 630px."
        ),
        required=False,
    )


@implementer(ISeo)
@adapter(IDexterityContent)
class Seo:
    def __init__(self, context):
        self.context = context
