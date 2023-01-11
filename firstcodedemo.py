from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
#chrome driver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait, expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from setuptools.command import upload

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://www.orioninc.com/careers/job-application/?job_id=16579")
driver.find_element(By.ID, "hs-eu-confirmation-button").click()
WebDriverWait(driver, 2)

#locators
#ID, Xpath, CSSelector, Classname, name, linktext
#static dropdown
driver.find_element(By.NAME, "input_2").send_keys(("Test"))
driver.find_element(By.NAME, "input_3").send_keys(("Test"))
driver.find_element(By.NAME, "input_4").send_keys("test.test@gmail.com")
driver.find_element(By.NAME, "input_5").send_keys("+37061234567")
WebDriverWait(driver, 2)
action = ActionChains(driver)
dropdown = driver.find_element(By.XPATH, "/html/body/main/article/div/div/div/div/div/div/form/div[2]/ul/li[6]/div/div/div[2]/b")
action.move_to_element(dropdown).click().perform()
country = WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, "/html/body/main/article/div/div/div/div/div/div/form/div[2]/ul/li[6]/div/div/div[3]/div/ul/li[128]")))
action.move_to_element(country).click().perform()
driver.find_element(By.NAME, "input_7").send_keys("Vilnius")
driver.find_element(By.NAME, "input_8").send_keys("Vilnius")
driver.find_element(By.NAME, "input_9").send_keys("LT1234")
driver.find_element(By.NAME, "input_11").send_keys("CV")
element = driver.find_element(By.ID, "input_7_12")
element.send_keys("C:\\Users\\vuziela\\TestCV.doc")
driver.find_element(By.NAME, "input_17").send_keys("Tech Muge")
browser = driver.find_element(By.ID, "label_7_13_1")
driver.find_element(By.ID, "label_7_13_1").click()
driver.find_element(By.ID, "gform_submit_button_7").click()











