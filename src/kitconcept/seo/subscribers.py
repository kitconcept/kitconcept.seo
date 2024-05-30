from kitconcept.seo.behaviors.seo import ISeo
from plone.dexterity.interfaces import IDexterityContent
from zope.component import adapter
from ZPublisher.interfaces import IPubAfterTraversal
from ZPublisher.pubevents import PubAfterTraversal


@adapter(IPubAfterTraversal)
def add_x_robots_noindex_header(event: PubAfterTraversal):
    """Add X-Robots-Tag to prevent indexing items with seo_noindex."""
    request = event.request
    for obj in request["PARENTS"]:
        if IDexterityContent.providedBy(obj):
            if ISeo.providedBy(obj) and obj.seo_noindex:
                request.response.setHeader("X-Robots-Tag", "noindex")
            break
