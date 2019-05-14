# -*- coding: utf-8 -*-
from kitconcept.seo.interfaces import IKitconceptSeoLayer
from kitconcept.seo.testing import KITCONCEPT_SEO_FUNCTIONAL_TESTING  # noqa
from plone.app.testing import setRoles
from plone.app.testing import SITE_OWNER_NAME
from plone.app.testing import SITE_OWNER_PASSWORD
from plone.app.testing import TEST_USER_ID
from plone.dexterity.fti import DexterityFTI
from plone.testing.z2 import Browser
from zope.interface import alsoProvides

import unittest


class SeoBehaviorFunctionalTest(unittest.TestCase):

    layer = KITCONCEPT_SEO_FUNCTIONAL_TESTING

    def setUp(self):
        app = self.layer["app"]
        self.portal = self.layer["portal"]
        self.request = self.layer["request"]
        self.portal_url = self.portal.absolute_url()
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        fti = DexterityFTI("seodocument")
        self.portal.portal_types._setObject("seodocument", fti)
        fti.klass = "plone.dexterity.content.Item"
        fti.behaviors = ("kitconcept.seo.behaviors.seo.ISeo",)
        self.fti = fti
        alsoProvides(self.portal.REQUEST, IKitconceptSeoLayer)
        alsoProvides(self.request, IKitconceptSeoLayer)
        from kitconcept.seo.behaviors.seo import ISeo

        alsoProvides(self.request, ISeo)
        self.portal.invokeFactory(
            "seodocument", id="seodocument", title=u"Document with SEO fields"
        )
        import transaction

        transaction.commit()
        # Set up browser
        self.browser = Browser(app)
        self.browser.handleErrors = False
        self.browser.addHeader(
            "Authorization",
            "Basic {0}:{1}".format(SITE_OWNER_NAME, SITE_OWNER_PASSWORD),
        )

    def test_seo_fieldset_in_edit_form(self):
        self.browser.open(self.portal_url + "/seodocument/edit")
        self.assertTrue("Override the meta title." in self.browser.contents)
        self.assertTrue(
            "Override the meta description" in self.browser.contents
        )  # noqa
        self.assertTrue("SEO" in self.browser.contents)
        self.assertTrue('<fieldset id="fieldset-seo"' in self.browser.contents)  # noqa

    def test_title_override_works(self):
        self.browser.open(self.portal_url + "/seodocument/edit")
        # todo: check title override
