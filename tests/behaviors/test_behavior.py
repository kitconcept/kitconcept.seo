def test_seo_behavior_fields(manager_plone_client):
    # Enable behavior for pages
    manager_plone_client.patch(
        "++api++/@controlpanels/dexterity-types/Document",
        json={"kitconcept.seo": True},
    )

    # Check schema
    schema = manager_plone_client.get("++api++/@types/Document").json()
    assert schema["fieldsets"][-1] == {
        "behavior": "plone",
        "description": "",
        "fields": [
            "seo_title",
            "seo_description",
            "seo_noindex",
            "seo_canonical_url",
            "opengraph_title",
            "opengraph_description",
            "opengraph_image",
        ],
        "id": "seo",
        "title": "SEO",
    }


def test_noindex_sets_response_header(manager_plone_client):
    # Enable behavior for pages
    manager_plone_client.patch(
        "++api++/@controlpanels/dexterity-types/Document",
        json={"kitconcept.seo": True},
    )

    # Add page
    resp = manager_plone_client.post(
        "++api++/",
        json={"@type": "Document", "title": "Test page", "seo_noindex": True},
    )
    assert resp.status_code == 201

    # Confirm the page is served with X-Robots-Tag header
    resp = manager_plone_client.get("/test-page")
    assert resp.status_code == 200
    assert resp.headers["X-Robots-Tag"] == "noindex"

    # Confirm views of the page are served with X-Robots-Tag header
    resp = manager_plone_client.get("/test-page/@@view")
    assert resp.status_code == 200
    assert resp.headers["X-Robots-Tag"] == "noindex"
