def test_seo_behavior_fields(manager_plone_client):
    # Enable behavior for pages
    manager_plone_client.patch(
        "/@controlpanels/dexterity-types/Document", json={"kitconcept.seo": True}
    )

    # Check schema
    schema = manager_plone_client.get("/@types/Document").json()
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
