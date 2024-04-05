import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service

driver = None

@pytest.fixture(params=['gecko','chrome'],scope='class')
def init_driver1(request):
    print("-------------------------browser launch-----------------------")
    if request.param=="chrome":
       chrome_driver_path = 'SeleniumClasses/chromedriver.exe'
       chrome_options = webdriver.ChromeOptions()
       service = Service(executable_path=chrome_driver_path)
       ch_driver = webdriver.Chrome(service=service, options=chrome_options)
    if request.param=="gecko":
        gecko_driver_path = 'SeleniumClasses/geckodriver.exe'
        gecko_options = webdriver.FirefoxOptions()
        service = Service(executable_path=gecko_driver_path)
        ch_driver = webdriver.Firefox(service=service, options=gecko_options)
    request.cls.driver = ch_driver
    yield
    print("-------------------------quit all browser-----------------------")
    ch_driver.quit()