import allure
import pytest as pytest
from selenium.webdriver.support.wait import WebDriverWait
from POM.pages.application_form import ApplicationForm

   #POM variables
input_first_name = 'Test'
input_last_name = 'Test'
input_email = 'test@test.gmail.com'
input_phone_number = '+37061234567'
input_country = 'Lithuania'
input_province = 'Vilnius'
input_city = 'Vilnius'
input_ZipCode = 'LT1234'
input_Skill_Summary = 'CV'
input_upload_cv = 'C:\\Users\\vuziela\\TestCV.doc'
input_About_Us = 'Tech Muge'
input_click_checkbox = 'Checkbox'
input_checkbox_is_selected = 1
input_submit = 'Submit Application'


@pytest.mark.usefixtures("setup")
class TestJobApplicationForm:

    @allure.severity(allure.severity_level.NORMAL)
    def test_firstname(self):
        self.applicationFormPage = ApplicationForm(self.driver)
        self.applicationFormPage.set_first_name(self.input_first_name)
        self.applicationFormPage.check_first_name_value(self.input_first_name)

    @allure.severity(allure.severity_level.NORMAL)
    def test_lastname(self):
        self.applicationFormPage = ApplicationForm(self.driver)
        self.applicationFormPage.set_last_name(self.input_last_name)
        self.applicationFormPage.check_last_name_value(self.input_last_name)

    @allure.severity(allure.severity_level.NORMAL)
    def test_email(self):
        self.applicationFormPage = ApplicationForm(self.driver)
        self.applicationFormPage.set_email(self.input_email)
        self.applicationFormPage.check_email_value(self.input_email)

    @allure.severity(allure.severity_level.NORMAL)
    def test_phone_number(self):
        self.applicationFormPage = ApplicationForm(self.driver)
        self.applicationFormPage.set_phone_number(self.input_phone_number)
        self.applicationFormPage.check_phone_number_value(self.input_phone_number)

    @allure.severity(allure.severity_level.NORMAL)
    def test_country(self):
        self.applicationFormPage = ApplicationForm(self.driver)
        self.applicationFormPage.set_country_list()
        WebDriverWait(self.driver, 5)
        self.applicationFormPage.select_country()
        self.applicationFormPage.check_country_value('Lithuania')

    @allure.severity(allure.severity_level.NORMAL)
    def test_province(self):
        self.applicationFormPage = ApplicationForm(self.driver)
        self.applicationFormPage.set_province(self.input_province)
        self.applicationFormPage.check_province_value(self.input_province)

    @allure.severity(allure.severity_level.MINOR)
    def test_city(self):
        self.applicationFormPage = ApplicationForm(self.driver)
        self.applicationFormPage.set_city(self.input_city)
        self.applicationFormPage.check_city_value(self.input_city)

    @allure.severity(allure.severity_level.MINOR)
    def test_zip_code(self):
        self.applicationFormPage = ApplicationForm(self.driver)
        self.applicationFormPage.set_zip_code(self.input_ZipCode)
        self.applicationFormPage.check_zip_code_value(self.input_ZipCode)

    @allure.severity(allure.severity_level.NORMAL)
    def test_skill_summary(self):
        self.applicationFormPage = ApplicationForm(self.driver)
        self.applicationFormPage.set_skill_summary(self.input_Skill_Summary)
        self.applicationFormPage.check_skill_summary_value(self.input_Skill_Summary)

    @allure.severity(allure.severity_level.NORMAL)
    def test_upload_cv(self):
        self.applicationFormPage = ApplicationForm(self.driver)
        self.applicationFormPage.upload_cv(self.input_upload_cv)
        self.applicationFormPage.check_upload_cv_value('TestCV.doc')

    @allure.severity(allure.severity_level.NORMAL)
    def test_about_us(self):
        self.applicationFormPage = ApplicationForm(self.driver)
        self.applicationFormPage.set_about_us(self.input_About_Us)
        self.applicationFormPage.check_about_us_value(self.input_About_Us)

    @allure.severity(allure.severity_level.NORMAL)
    def test_save_my_info_checkbox(self):
        self.applicationFormPage = ApplicationForm(self.driver)
        self.applicationFormPage.click_checkbox()
        self.applicationFormPage.check_checkbox_value(1)

    @allure.severity(allure.severity_level.CRITICAL)
    def test_submit_application(self):
        self.applicationFormPage = ApplicationForm(self.driver)
        self.applicationFormPage.select_submit()
        self.applicationFormPage.check_submit_value(self.input_submit)
