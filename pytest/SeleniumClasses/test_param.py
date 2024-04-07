import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service


@pytest.fixture(params=['chrome','gecko'],scope='class')
def init_driver(request):
    global ch_driver
    print("-------------------------browser launch-----------------------")
    if request.param=="chrome":
        chrome_driver_path = 'SeleniumClasses/chromedriver.exe'
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless=new")
        service = Service(executable_path=chrome_driver_path)
        ch_driver = webdriver.Chrome(service=service, options=chrome_options)
    if request.param=="gecko":
        gecko_driver_path = 'SeleniumClasses/geckodriver.exe'
        gecko_options = webdriver.FirefoxOptions()
        service = Service(executable_path=gecko_driver_path)
        ch_driver = webdriver.Firefox(service=service, options=gecko_options)
    request.cls.driver = ch_driver
    ch_driver.implicitly_wait(30)
    yield
    print("-------------------------quit all browser-----------------------")
    ch_driver.quit()


@pytest.mark.usefixtures("init_driver")
class BaseTest():
    pass


class TestHubspot(BaseTest):

   @pytest.mark.parametrize("username1, password1",
                           [
                               ('bewarepretty@gmail.com','Active@2024')
                           ])
   def test_login(self,username1,password1):
         self.driver.get("https://www.hubspot.com/login")
         self.driver.find_element(By.ID,"username").send_keys(username1)
         self.driver.find_element(By.ID,"password").send_keys(password1)




