import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = None

@pytest.fixture(params=['chrome'],scope='class')
def init_driver(request):
    print("-------------------------browser launch-----------------------")
    if request.param=="chrome":
       chrome_driver_path = 'SeleniumClasses/chromedriver.exe'
       chrome_options = webdriver.ChromeOptions()
       service = Service(executable_path=chrome_driver_path)
       ch_driver = webdriver.Chrome(service=service, options=chrome_options)
       request.cls.driver = ch_driver
    yield
    print("-------------------------quit all browser-----------------------")
    ch_driver.quit()

@pytest.mark.usefixtures("init_driver")
class base_chrome():
    pass

class Test_Google(base_chrome):

   def test_google_title(self):
      self.driver.get("https://www.google.com")
      assert self.driver.title == 'Google'