from kitconcept.seo.testing import FUNCTIONAL_TESTING
from kitconcept.seo.testing import INTEGRATION_TESTING
from plone.app.testing import SITE_OWNER_NAME
from plone.app.testing import SITE_OWNER_PASSWORD
from plone.restapi.testing import RelativeSession
from pytest_plone import fixtures_factory
import pytest


pytest_plugins = ["pytest_plone"]


globals().update(
    fixtures_factory(
        (
            (FUNCTIONAL_TESTING, "functional"),
            (INTEGRATION_TESTING, "integration"),
        )
    )
)


@pytest.fixture
def manager_plone_client(functional):
    portal = functional["portal"]
    api_session = RelativeSession(f"{portal.absolute_url()}/++api++")
    api_session.auth = (SITE_OWNER_NAME, SITE_OWNER_PASSWORD)
    return api_session
