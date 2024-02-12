import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

import time
import os
from os import walk

from utilities import read_configuration


@pytest.fixture()
def setup_and_teardown(request):
    config = read_configuration()

    appium_server_url = config["general"]["local"]["server_url"]
    platform_name = config["general"]["platform_name"]
    device_name = config["general"]["device_name"]
    app = config["general"]["app"]

    app = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")), app)

    capabilities = {
        "platformName": platform_name,
        "appium:deviceName": device_name,
        "appium:app": app,
    }

    # Converts capabilities to AppiumOptions instance
    capabilities_options = UiAutomator2Options().load_capabilities(capabilities)

    # Start webdriver
    driver = webdriver.Remote(command_executor=appium_server_url, options=capabilities_options)

    request.cls.driver = driver
    time.sleep(0.5)
    yield
    driver.quit()
