from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage
import time
import pytest
from testData.HomePageData import HomePageData

class TestHomePage(BaseClass):

    def test_form_submission(self,get_data):
        log = self.get_Logger()
        homepage= HomePage(self.driver)
        log.info("first name : "+get_data['firstname'])
        homepage.get_name().send_keys(get_data['firstname'])
        time.sleep(2)
        homepage.get_email().send_keys(get_data['email'])
        time.sleep(2)
        homepage.get_password().send_keys(get_data['password'])
        time.sleep(2)
        homepage.get_checkbox1().click()
        time.sleep(2)
        self.select_gender_from_dropdown(homepage.get_dropdown(),get_data['gender'])
        time.sleep(2)
        homepage.get_success_btn().click()
        time.sleep(2)
        message = homepage.get_success_alert().text
        time.sleep(2)
        print("Message displayed on alert is\n",message)
        time.sleep(2)
        #assert "Success" in message
        assert "qwerty" in message
        time.sleep(2)
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def get_data(self,request):
        return request.param

