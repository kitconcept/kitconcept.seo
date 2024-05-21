from kitconcept.seo import PACKAGE_NAME


class TestSetupInstall:
    def test_addon_installed(self, installer):
        """Test if kitconcept.seo is installed."""
        assert installer.is_product_installed(PACKAGE_NAME) is True

    def test_browserlayer(self, browser_layers):
        """Test that IKitconceptSeoLayer is registered."""
        from kitconcept.seo.interfaces import IKitconceptSeoLayer

        assert IKitconceptSeoLayer in browser_layers

    def test_latest_version(self, profile_last_version):
        """Test latest version of default profile."""
        assert profile_last_version(f"{PACKAGE_NAME}:default") == "1000"
