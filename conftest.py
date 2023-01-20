import allure
import pytest as pytest
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
# from selenium.webdriver.chrome import webdriver
# from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait, expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import elements_selectors
import text_variables


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(executable_path="C:\\Users\\vuziela\\AppData\\Local\\Programs\\Python\\Python37\\Scripts\\chromedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://www.orioninc.com/careers/job-application/?job_id=16579")
    driver.find_element(By.ID, elements_selectors.cookies).click()
    WebDriverWait(driver, 2)
    request.cls.driver = driver
    yield
    driver.close()