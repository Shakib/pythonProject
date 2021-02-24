from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import *
from selenium import *
import time

# För att generaera Allurt test report ska skriva i command line följande script:
# behave -f allure_behave.formatter:AllureFormatter -o reports/ features
# Efter ovan command måste igen skriva : allure generate reports/   ->för att konverter json filer till HTMML format
# Sedan copiera index.html länken och klistra in i Firefox Nightly

@given(u'I launch chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


@when(u'I open orange HRM homepage')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")
    time.sleep(1)

@when(u'Enter username "{User}" and password "{pwd}"')
def step_impl(context, User, pwd):
    context.driver.find_element_by_id("txtUsername").send_keys(User)
    context.driver.find_element_by_id("txtPassword").send_keys(pwd)
    time.sleep(1)


@when(u'Click on login button')
def step_impl(context):
    context.driver.find_element_by_id("btnLogin").click()
    time.sleep(1)

@then(u'User must successfully login to the Dashboard page')
def step_impl(context):
    try:
        text = context.driver.find_element_by_xpath("//*[@id='content']/div/div[1]/h1").text
    except:
        time.sleep(1)
        context.driver.close()
        assert False, "Test Failed"
    if text == "Dashboard":
        context.driver.close()
        assert True, "Test Passed"


