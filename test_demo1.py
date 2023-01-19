import pytest as pytest
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait, expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import elements_selectors
import text_variables


@pytest.mark.usefixtures("setup")
class TestExample:

    def test_FirstName(self):
        self.driver.find_element(By.NAME, elements_selectors.FirstName).send_keys("Test")
        text = self.driver.find_element(By.ID, text_variables.text_FirstName).get_attribute("value")
        assert text == "Test"
        print(text)

    def test_LastName(self):
        self.driver.find_element(By.NAME, elements_selectors.LastName).send_keys("Test")
        text = self.driver.find_element(By.ID, text_variables.text_LastName).get_attribute("value")
        assert text == "Test"
        print(text)

    def test_email(self):
        self.driver.find_element(By.NAME, elements_selectors.Email).send_keys("test.test@gmail.com")
        text = self.driver.find_element(By.ID, text_variables.text_Email).get_attribute("value")
        assert text == "test.test@gmail.com"
        print(text)

    def test_PhoneNumber(self):
        self.driver.find_element(By.NAME, elements_selectors.PhoneNumber).send_keys("+37061234567")
        text = self.driver.find_element(By.ID, text_variables.text_PhoneNumber).get_attribute("value")
        assert text == "+37061234567"
        print(text)

    def test_Country(self):
        action = ActionChains(self.driver)
        dropdown = self.driver.find_element(By.XPATH, elements_selectors.countrylist)
        action.move_to_element(dropdown).click().perform()
        country = WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, elements_selectors.Country)))
        action.move_to_element(country).click().perform()
        text = self.driver.find_element(By.ID, text_variables.text_Country).get_attribute("value")
        assert text == "Lithuania"
        print(text)

    def test_City1(self):
        self.driver.find_element(By.NAME, elements_selectors.City).send_keys("Vilnius")
        text = self.driver.find_element(By.ID, text_variables.text_city1).get_attribute("value")
        assert text == "Vilnius"
        print(text)

    def test_City2(self):
        self.driver.find_element(By.NAME, elements_selectors.City1).send_keys("Vilnius")
        text = self.driver.find_element(By.ID, text_variables.text_city2).get_attribute("value")
        assert text == "Vilnius"
        print(text)

    def test_Zip(self):
        self.driver.find_element(By.NAME, elements_selectors.Zip).send_keys("LT1234")
        text = self.driver.find_element(By.ID, text_variables.text_Zip).get_attribute("value")
        assert text == "LT1234"
        print(text)

    def test_SkillSummary(self):
        self.driver.find_element(By.NAME, elements_selectors.SkillSummary).send_keys("CV")
        text = self.driver.find_element(By.ID, text_variables.text_SkillSummary).get_attribute("value")
        assert text == "CV"
        print(text)

    def test_UploadCV(self):
        element = self.driver.find_element(By.ID, elements_selectors.CV)
        element.send_keys("C:\\Users\\vuziela\\TestCV.doc")
        text = self.driver.find_element(By.XPATH, text_variables.text_CVUploaded).text
        assert text == "TestCV.doc"
        print("CVUploaded", text)

    def test_AboutUs(self):
        self.driver.find_element(By.NAME, elements_selectors.AboutUs).send_keys("Tech Muge")
        text = self.driver.find_element(By.ID, text_variables.text_TechMuge).get_attribute("value")
        assert text == "Tech Muge"
        print(text)

    def test_SaveMyInfoCheckbox(self):
        self.driver.find_element(By.ID, elements_selectors.SaveMyInfoCheckbox).click()
        text = self.driver.find_element(By.ID, text_variables.text_Checkbox).text
        assert text == "Save my information"
        print(text)

    def test_SubmitApplication(self):
        self.driver.find_element(By.ID, elements_selectors.Submit).click()
        text = self.driver.find_element(By.ID, text_variables.text_SubmitApplication).get_attribute("value")
        assert text == "Submit Application"
        print(text)






