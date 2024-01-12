"""Setup tests for this package."""
from kitconcept.seo.testing import KITCONCEPT_SEO_INTEGRATION_TESTING  # noqa
from Products.CMFPlone.utils import get_installer

import unittest


class TestSetup(unittest.TestCase):
    """Test that kitconcept.seo is properly installed."""

    layer = KITCONCEPT_SEO_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        self.installer = get_installer(self.portal)

    def test_product_installed(self):
        self.assertTrue(self.installer.is_product_installed("kitconcept.seo"))

    def test_browserlayer(self):
        """Test that IKitconceptSeoLayer is registered."""
        from kitconcept.seo.interfaces import IKitconceptSeoLayer
        from plone.browserlayer import utils

        self.assertIn(IKitconceptSeoLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):
    layer = KITCONCEPT_SEO_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.installer = get_installer(self.portal, self.layer["request"])
        self.installer.uninstall_product("kitconcept.seo")

    def test_product_uninstalled(self):
        """Test if kitconcept.seo is cleanly uninstalled."""
        self.assertFalse(self.installer.is_product_installed("kitconcept.seo"))

    def test_browserlayer_removed(self):
        """Test that IKitconceptSeoLayer is removed."""
        from kitconcept.seo.interfaces import IKitconceptSeoLayer
        from plone.browserlayer import utils

        self.assertNotIn(IKitconceptSeoLayer, utils.registered_layers())
