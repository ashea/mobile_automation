import pytest
import time

from pages.mobile_pages.sign_in_page import SignInPage
from pages.mobile_pages.service_page import ServicePage


class BaseTest(object):
    sign_in_page = SignInPage()
    service_page = ServicePage()

    @pytest.fixture(autouse=True, scope="function")
    def setUpClass(self):
        self.sign_in_page.login_if_needed()

    @classmethod
    def teardown_class(self):
        self.service_page.close_driver_if_needed()
