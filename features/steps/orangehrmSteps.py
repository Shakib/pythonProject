from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


@given('Launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    #context.driver = webdriver.Chrome(executable_path="C:\\Users\\Administrator\\Downloads\\chromedriver_win32\\chromedriver.exe")



@when('Open orange hrm homepage')
def openHomepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@then('Verify that the logo present on page')
def verifyLogo(context):
    status = context.driver.find_element_by_id("divLogo").is_displayed()
    assert status is True


@then('Close browser')
def closeBrowser(context):
    context.driver.close()
