import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

import elements_selectors
import text_variables
from POM.pages.base_page import BasePage


class ApplicationForm(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    FirstName = (By.NAME, elements_selectors.FirstName)
    LastName = (By.NAME, elements_selectors.LastName)
    Email = (By.NAME, elements_selectors.Email)
    PhoneNumber = (By.NAME, elements_selectors.PhoneNumber)
    Province = (By.NAME, elements_selectors.Province)
    City = (By.NAME, elements_selectors.City)
    ZipCode = (By.NAME, elements_selectors.ZipCode)
    SkillSummary = (By.NAME, elements_selectors.SkillSummary)
    CV = (By.ID, elements_selectors.CV)
    AboutUs = (By.NAME, elements_selectors.AboutUs)
    SaveMyInfoCheckBoxClick = (By.ID, elements_selectors.SaveMyInfoCheckbox)
    CheckboxIsSelected = (By.ID, elements_selectors.Checkbox)
    Submit = (By.ID, elements_selectors.Submit)
    CVupload = (By.XPATH, elements_selectors.UploadCV)
    Country_list = (By.XPATH, elements_selectors.countrylist)
    Country = (By.ID, text_variables.text_Country)

    #First Name
    def set_first_name(self, firstname):
        self.send_keys(self.FirstName, firstname)

    def get_first_name_value(self):
        return self.get_value_attribute(self.FirstName)

    def check_first_name_value(self, expected_first_name):
        actual_first_name = self.get_first_name_value()
        assert actual_first_name == expected_first_name

    #Last Name
    def set_last_name(self, lastname):
        self.send_keys(self.LastName, lastname)

    def get_last_name_value(self):
        return self.get_value_attribute(self.LastName)

    def check_last_name_value(self, expected_last_name):
        actual_last_name = self.get_last_name_value()
        assert actual_last_name == expected_last_name

    #Email
    def set_email(self, email):
        self.send_keys(self.Email, email)

    def get_email_value(self):
        return self.get_value_attribute(self.Email)

    def check_email_value(self, expected_email):
        actual_email = self.get_email_value()
        assert actual_email == expected_email

        #PhoneNumber
    def set_phone_number(self, phone_number):
        self.send_keys(self.PhoneNumber, phone_number)

    def get_phone_number_value(self):
        return self.get_value_attribute(self.PhoneNumber)

    def check_phone_number_value(self, expected_phone_number):
        actual_phone_number = self.get_phone_number_value()
        assert actual_phone_number == expected_phone_number

        #Country

    def set_country_list(self):
        self.click(self.Country_list)

    def get_country_value(self):
        return self.get_value_attribute(self.Country)

    def check_country_value(self, value):
        assert self.get_country_value() == value

    def select_country(self):
        action = ActionChains(self.driver)
        lit = self.driver.find_element(By.XPATH, elements_selectors.Country)
        action.move_to_element(lit).click().perform()

       #Province
    def set_province(self, province):
        self.send_keys(self.Province, province)

    def get_province_value(self):
        return self.get_value_attribute(self.Province)

    def check_province_value(self, expected_province):
        actual_province = self.get_province_value()
        assert actual_province == expected_province

        #City

    def set_city(self, city):
        self.send_keys(self.City, city)

    def get_city_value(self):
        return self.get_value_attribute(self.City)

    def check_city_value(self, expected_city):
        actual_city = self.get_city_value()
        assert actual_city == expected_city

        #Zip

    def set_zip_code(self, zip_code):
        self.send_keys(self.ZipCode, zip_code)

    def get_zip_code_value(self):
        return self.get_value_attribute(self.ZipCode)

    def check_zip_code_value(self, expected_zip_code):
        actual_zip_code = self.get_zip_code_value()
        assert actual_zip_code == expected_zip_code

        #SkillSumarry
    def set_skill_summary(self, skill_summary):
        self.send_keys(self.SkillSummary, skill_summary)

    def get_skill_summary_value(self):
        return self.get_value_attribute(self.SkillSummary)

    def check_skill_summary_value(self, expected_skill_summary):
        actual_skill_summary = self.get_skill_summary_value()
        assert actual_skill_summary == expected_skill_summary

        #UploadCV
    def upload_cv(self, upload_cv):
        self.send_keys(self.CV, upload_cv)

    def get_upload_cv_value(self):
        return self.get_text(self.CVupload)

    def check_upload_cv_value(self, value):
        assert self.get_upload_cv_value() == value

        #AboutUs
    def set_about_us(self, about_us):
        self.send_keys(self.AboutUs, about_us)

    def get_about_us_value(self):
        return self.get_value_attribute(self.AboutUs)

    def check_about_us_value(self, expected_about_us):
        actual_about_us = self.get_about_us_value()
        assert actual_about_us == expected_about_us

    #SaveMyInfoCheckBox
    def click_checkbox(self):
        self.click(self.SaveMyInfoCheckBoxClick)

    def checkbox_is_selected_value(self):
        return self.get_value_attribute(self.CheckboxIsSelected)

    def check_checkbox_value(self, value):
        assert self.get_checkbox_value(self.CheckboxIsSelected) == value

    #Submit

    def select_submit(self):
        self.click(self.Submit)

    def get_submit_value(self):
        return self.get_value_attribute(self.Submit)

    def check_submit_value(self, expected_submit):
        actual_submit = self.get_submit_value()
        assert actual_submit == expected_submit
