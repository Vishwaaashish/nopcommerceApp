import time

import pytest

from pageobject.loginpage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils

class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path=".//TestData/LoginData.xlxs"
    logger = LogGen.loggen()

    # @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logger.info("**********Test_002_DDT_Login************")
        self.logger.info("********Verifying login DDt Test*********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)

        self.rows=XLUtils.getRowCount(self.path,'sheet1')
        print("Number of rows in a excel:",self.rows)

        list_status=[]

        for r in range(2,self.rows+1):
            self.user=XLUtils.readData(self.path,'sheet1',r,1)
            self.password = XLUtils.readData(self.path,'sheet1',r,2)
            self.exp = XLUtils.readData(self.path, 'sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(3)

            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"
            if act_title==exp_title:
                if self.exp=="Pass":
                    self.logger.info("***passed***")
                    self.lp.clickLogout()
                    list_status.append("Pass")
                elif self.exp=="Fail":
                    self.logger.info("***failed****")
                    self.lp.clickLogout()
                    list_status.append("failed")

            elif act_title != exp_title:
                if self.exp=="Pass":
                    self.logger.info("***failed***")
                    list_status.append("Fail")
                elif self.exp=="Fail":
                    self.logger.info("***passed****")
                    list_status.append("Pass")

        if "Fail" not in list_status:
            self.logger.info("******* Login DDt test passed ********")
            self.driver.close()
            assert True
        else:
            self.logger.info("******* Login DDT test failed*********")
            self.driver.close()
            assert False

        self.logger.info("********* End of Login DDT Test*************")
        self.logger.info("********* CompletedTC_ LoginDDT_002*************")








