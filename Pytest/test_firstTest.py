from allure_commons.types import AttachmentType
from selenium import webdriver
import pytest
import allure_pytest
import allure
import time

@allure.severity(allure.severity_level.MINOR)
class TestNO1:
    @allure.severity(allure.severity_level.MINOR)
    def test_openChrome(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.maximize_window()
        allure.attach(self.driver.get_screenshot_as_png(), name="testLogins", attachment_type=AttachmentType.PNG)  # För att ta screenshot
        time.sleep(2)
        self.driver.close()




# Det finns så kallas Decorator som används så här:
# @allure.severity(allure.severity_Level.NORMAL
# Kolla på den här youtou tutorial   https://www.youtube.com/watch?v=kP-PnWBJPqA