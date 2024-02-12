import pytest


@pytest.mark.usefixtures("setup_and_teardown")
class BaseTest:

    # function that can be accessed by any Test class that inherited from the BaseTest class
    def template_method(self):
        pass
