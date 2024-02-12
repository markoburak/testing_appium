from components.comp_shared import CompShared


class InitialSelectors:
    selectors = {}
    selectors['rate_this_app_panel'] = "//*[@resource-id='com.ogden.memo:id/parentPanel']"
    selectors['rate_this_app_title'] = "//*[@resource-id='com.ogden.memo:id/alertTitle']"
    selectors['rate_this_app_message'] = "//*[@resource-id='com.ogden.memo:id/alertMessage']"
    selectors['rate_this_app_no_thanks_button'] = "//*[@resource-id='android:id/button2']"


class InitialPage(CompShared, InitialSelectors):
    def __init__(self, driver):
        super().__init__(driver)

    def rate_this_app_panel_displayed(self) -> bool:
        return self.check_display_status_of_element(selector=self.selectors['rate_this_app_panel'])
    def get_initial_message(self) -> str:
        return self.get_element_text(selector=self.selectors['rate_this_app_title'])

    def click_no_thanks(self) -> None:
        return self.click_element(selector=self.selectors['rate_this_app_no_thanks_button'])
