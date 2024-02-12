from Test_cases.TestConfig.base import BaseTest
from components.init_page import InitialPage


class TestInitial(BaseTest):
    driver = None

    def test_rate_this_app(self):
        initial_page = InitialPage(self.driver)

        assert initial_page.rate_this_app_panel_displayed() is True
        assert initial_page.get_initial_message() == "Rate this app"

    def test_rate_this_app_no_thanks(self):
        initial_page = InitialPage(self.driver)

        assert initial_page.rate_this_app_panel_displayed() is True

        initial_page.click_no_thanks()

        assert initial_page.rate_this_app_panel_displayed() is False
