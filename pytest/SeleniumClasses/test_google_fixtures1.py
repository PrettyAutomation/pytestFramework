import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = None

@pytest.fixture(scope='module')
def init_driver():
    global driver
    print("-------------------------browser launch-----------------------")
    chrome_driver_path = 'SeleniumClasses/chromedriver.exe'
    chrome_options = webdriver.ChromeOptions()
    service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    yield
    print("-------------------------quit all browser-----------------------")
    driver.quit()


# def test_google(init_driver):
#     driver.get("https://www.google.com")
#     assert driver.title=='Google'
#
#
# def test_stackoverflow(init_driver):
#     driver.get("http://stackoverflow.com")
#     assert driver.title=="Stack Overflow - Where Developers Learn, Share, & Build Careers"

@pytest.mark.usefixtures("init_driver")
def test_google():
    driver.get("https://www.google.com")
    assert driver.title=='Google'

@pytest.mark.usefixtures("init_driver")
def test_stackoverflow():
    driver.get("http://stackoverflow.com")
    assert driver.title=="Stack Overflow - Where Developers Learn, Share, & Build Careers"
