from kitconcept.seo.behaviors.seo import ISeo
from zope.component import adapter
from ZPublisher.interfaces import IPubAfterTraversal
from ZPublisher.pubevents import PubAfterTraversal


@adapter(IPubAfterTraversal)
def add_x_robots_noindex_header(event: PubAfterTraversal):
    """Add X-Robots-Tag to prevent indexing items with seo_noindex."""
    request = event.request
    context = request["PARENTS"][0]
    if ISeo.providedBy(context) and context.seo_noindex:
        request.response.setHeader("X-Robots-Tag", "noindex")
