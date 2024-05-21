from kitconcept.seo import PACKAGE_NAME

import pytest


class TestSetupUninstall:
    @pytest.fixture(autouse=True)
    def uninstalled(self, installer):
        installer.uninstall_product(PACKAGE_NAME)

    def test_addon_uninstalled(self, installer):
        """Test if kitconcept.seo is uninstalled."""
        assert installer.is_product_installed(PACKAGE_NAME) is False

    def test_browserlayer_not_registered(self, browser_layers):
        """Test that IKitconceptSeoLayer is not registered."""
        from kitconcept.seo.interfaces import IKitconceptSeoLayer

        assert IKitconceptSeoLayer not in browser_layers
