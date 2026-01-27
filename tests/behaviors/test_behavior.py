from copy import deepcopy
from kitconcept.seo import PACKAGE_NAME

import pytest


PAYLOAD = {
    "seo_title": "Foo Bar",
    "seo_description": "Lorem ipsum dolor sit amet",
    "seo_noindex": False,
    "seo_canonical_url": "https://example.com/canonical-url",
    "opengraph_title": "Open Graph Title",
    "opengraph_description": "Open Graph Description",
    "opengraph_image": None,
}


@pytest.fixture
def payload() -> dict:
    data = deepcopy(PAYLOAD)
    return data


class TestBehaviorContato:
    name: str = f"{PACKAGE_NAME}"

    @pytest.fixture(autouse=True)
    def _setup(self, portal_factory, dummy_type_schema, manager_html_request):
        self.portal = portal_factory(behavior=self.name)
        self.schema = dummy_type_schema()
        self.request = manager_html_request

    @pytest.mark.parametrize("key", PAYLOAD.keys())
    def test_behavior_schema(self, key: str):
        assert key in self.schema["properties"]

    def test_behavior_data(self, payload: dict, create_dummy_content):
        response = create_dummy_content(payload)
        assert response.status_code == 201

    def test_noindex_sets_response_header(self):
        # Add page
        resp = self.request.post(
            "++api++/",
            json={"@type": "DummyType", "title": "Test page", "seo_noindex": True},
        )
        assert resp.status_code == 201

        # Confirm the page is served with X-Robots-Tag header
        resp = self.request.get("/test-page")
        assert resp.status_code == 200
        assert resp.headers["X-Robots-Tag"] == "noindex"

        # Confirm views of the page are served with X-Robots-Tag header
        resp = self.request.get("/test-page/@@view")
        assert resp.status_code == 200
        assert resp.headers["X-Robots-Tag"] == "noindex"
