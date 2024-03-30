from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def test_google():
    chrome_driver_path = 'SeleniumClasses/chromedriver.exe'
    chrome_options = webdriver.ChromeOptions()
    service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get("https://www.google.com")
    assert driver.title=='Google'


def test_stackoverflow():
    chrome_driver_path = 'SeleniumClasses/chromedriver.exe'
    chrome_options = webdriver.ChromeOptions()
    service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get("http://stackoverflow.com")
    driver.quit()