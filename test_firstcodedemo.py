from selenium.webdriver import ActionChains

from selenium.webdriver.support import wait, expected_conditions


from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait



import elements_selectors

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://www.orioninc.com/careers/job-application/?job_id=16579")

driver.find_element(By.ID, elements_selectors.cookies).click()

WebDriverWait(driver, 2)
driver.find_element(By.NAME, elements_selectors.FirstName).send_keys("Test")
driver.find_element(By.NAME, elements_selectors.LastName).send_keys("Test")
driver.find_element(By.NAME, elements_selectors.Email).send_keys("test.test@gmail.com")
driver.find_element(By.NAME, elements_selectors.PhoneNumber).send_keys("+37061234567")

WebDriverWait(driver, 2)
action = ActionChains(driver)
dropdown = driver.find_element(By.XPATH, elements_selectors.countrylist)
action.move_to_element(dropdown).click().perform()
country = WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, elements_selectors.Country)))
action.move_to_element(country).click().perform()

driver.find_element(By.NAME, elements_selectors.City).send_keys("Vilnius")
driver.find_element(By.NAME, elements_selectors.City1).send_keys("Vilnius")
driver.find_element(By.NAME, elements_selectors.Zip).send_keys("LT1234")
driver.find_element(By.NAME, elements_selectors.SkillSummary).send_keys("CV")
element = driver.find_element(By.ID, elements_selectors.CV)

element.send_keys("C:\\Users\\vuziela\\TestCV.doc")

driver.find_element(By.NAME, elements_selectors.AboutUs).send_keys("Tech Muge")
browser = driver.find_element(By.ID, elements_selectors.SaveMyInfoCheckbox)
driver.find_element(By.ID, elements_selectors.SaveMyInfoCheckbox).click()
driver.find_element(By.ID, elements_selectors.Submit).click()











