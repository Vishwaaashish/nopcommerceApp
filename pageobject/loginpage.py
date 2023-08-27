from selenium.webdriver.common.by import By
class LoginPage:

    def __init__(self,driver):
        self.driver=driver
        self.textbox_username = (By.XPATH, "//input[@id='Email']")
        self.textbox_password = (By.XPATH, "//input[@id='Password']")
        self.button_login = (By.XPATH, "//button[@type='submit']")
        self.link_logout = (By.XPATH, "//a[normalize-space()='Logout']")

    def setUserName(self,username):
        self.driver.find_element(*self.textbox_username).clear()
        self.driver.find_element(*self.textbox_username).send_keys(username)
    def setPassword(self, password):
        self.driver.find_element(*self.textbox_password).clear()
        self.driver.find_element(*self.textbox_password).send_keys(password)
    def clickLogin(self):
        self.driver.find_element(*self.button_login).click()

    def clickLogout(self):
        self.driver.find_element(*self.link_logout).click()
