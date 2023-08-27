import string
import random

import pytest

from pageobject.AddcustomerPage import AddCustomer
from pageobject.loginpage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.webdriver.common.by import By


class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    # @pytest.mark.sanity
    def test_addCustomer(self,setup):
        self.logger.info("***********Test_003_AddCustomer*************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***********login Succesfull*************")

        self.logger.info("***********Starting Add Customer Test*************")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItems()

        self.addcust.clickOnAddnew()

        self.logger.info("***********providing Customer Info*************")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setCustomersRoles("Registered")
        self.addcust.setDrpVendors("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("Aashish")
        self.addcust.setLastName("Vishwakarma")
        self.addcust.setDob("03/16/1994")
        self.addcust.setCompanyName("Amazon")
        self.addcust.setAdminContent("This is for testing")
        self.addcust.clickOnSave()

        self.logger.info("******** Saving customer info *********")

        self.logger.info("******** Add customer validation started *********")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("********** Add customer Test Passed************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")
            self.logger.error("********* Add customer Test Failed**********")
            assert True == False

        self.driver.close()
        self.logger.info("********* Ending Home Page Title Test**********")

def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))







