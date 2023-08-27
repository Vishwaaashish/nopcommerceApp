import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class AddCustomer:
    def __init__(self,driver):
        self.driver = driver
        self.lnkCustomer_menu = (By.XPATH, "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a/p")
        self.lnkCustomer_menuitem = (By.XPATH, "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p")
        self.btnAddnew = (By.XPATH, "//a[@class='btn btn-primary']")
        self.txtEmail=(By.XPATH, "//input[@id='Email']")
        self.txtPassword=(By.XPATH, "//input[@id='Password']")
        self.txtFirstName = (By.XPATH, "//input[@id='FirstName']")
        self.txtLastName = (By.XPATH, "//input[@id='LastName']")
        self.rdMaleGender = (By.XPATH, "//input[@id='Gender_Male']")
        self.rdFemaleGender = (By.XPATH, "//input[@id='Gender_Female']")
        self.txtDob = (By.XPATH, "//input[@id='DateOfBirth']")
        self.txtCompanyName = (By.XPATH, "//input[@id='Company']")

        self.txtcustomerRoles = (By.XPATH, "//div[@class='input-group-append input-group-required']//div[@role='listbox']")
        self.lstitemAdministrators = (By.XPATH, "//ul[@id='SelectedCustomerRoleIds_taglist']")
        self.lstitemRegisterd = (By.XPATH, "//li[normalize-space()='Registered']")
        self.lstitemGuests = (By.XPATH, "//li[normalize-space()='Guests']")
        self.lstitemVendors = (By.XPATH, "//select[@id='VendorId']")
        self.drpmgrofVendors = (By.XPATH, "//select[@id='VendorId']")
        self.txtAdminContent = (By.XPATH, "//textarea[@id='AdminComment']")
        self.btnSave = (By.XPATH, "//button[@name='save']//i[@class='far fa-save']")

    # def __init__(self, driver):
    #     self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element(*self.lnkCustomer_menu).click()

    def clickOnCustomersMenuItems(self):
        self.driver.find_element(*self.lnkCustomer_menuitem).click()

    def clickOnAddnew(self):
        self.driver.find_element(*self.btnAddnew).click()
        
    def setEmail(self,email):
        self.driver.find_element(*self.txtEmail).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(*self.txtPassword).send_keys(password)

    def setCustomersRoles(self,role):
        self.driver.find_element(*self.txtcustomerRoles).click()
        time.sleep(3)
        if role=='Registered':
        # if role == 'Registered':
        #     self.listitem = self.driver.find_element(*self.lstitemRegisterd)
        # elif role=='Administrators':
        #     self.listitem = self.driver.find_element(*self.lstitemAdministrators)
        # elif role=='Guests':
        #     time.sleep(3)
        #     self.driver.find_element(By.XPATH,"//span[@title='delete']").click()
        #     self.listitem = self.driver.find_element(*self.lstitemGuests)
        # elif role=='Registered':
        #     self.listitem = self.driver.find_element(*self.lstitemRegisterd)
        # elif role=='Vendors':
        #     self.listitem = self.driver.find_element(*self.lstitemVendors)
        # else:
            self.listitem = self.driver.find_element(*self.lstitemRegisterd)
        #     time.sleep(3)
            self.driver.execute_script("arguments[0].click();",self.listitem)

    def setDrpVendors(self, value):
        drp=Select(self.driver.find_element(*self.drpmgrofVendors))
        drp.select_by_visible_text(value)

    def setGender(self, gender):
        if gender=='Male':
            self.driver.find_element(*self.rdMaleGender).click()
        elif gender=='Female':
            self.driver.find_element(*self.rdFemaleGender).click()
        else:
            self.driver.find_element(*self.rdMaleGender).click()

    def setFirstName(self,fname):
        self.driver.find_element(*self.txtFirstName).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(*self.txtLastName).send_keys(lname)

    def setDob(self,dob):
        self.driver.find_element(*self.txtDob).send_keys(dob)

    def setCompanyName(self,comname):
        self.driver.find_element(*self.txtCompanyName).send_keys(comname)

    def setAdminContent(self, content):
        self.driver.find_element(*self.txtAdminContent).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(*self.btnSave).click()

