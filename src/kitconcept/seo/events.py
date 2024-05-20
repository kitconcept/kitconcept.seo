from plone.app.contenttypes.interfaces import IImage
from zope.component import adapter
from ZPublisher.interfaces import IPubAfterTraversal
from ZPublisher.pubevents import PubAfterTraversal


@adapter(IPubAfterTraversal)
def after_image_pub_traversal(event: PubAfterTraversal):
    """Record the view as the HTTP route after traversal"""
    request = event.request
    context = event.request["PARENTS"][0]
    if IImage.providedBy(context):
        request.response.setHeader("X-Robots-Tag", "noindex")
