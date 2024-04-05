import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service

@pytest.fixture()
def input_total1():
    total = 100
    return total

@pytest.fixture()
def input_total2():
    total = 90
    return total

