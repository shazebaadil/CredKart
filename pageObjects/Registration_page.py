from selenium.webdriver.common.by import By

from pageObjects.Login_page import LoginPage
# Click on Register link
# Enter Name
# Enter Email
# Enter password
#confirm password
#click on reg button
#verfy


class RegistrationPage(LoginPage):
    text_name_id="name"
    text_confirm_password_id="password-confirm"

    def __init__(self,driver):
        self.driver=driver


    def enter_name(self,name):
        self.driver.find_element(By.ID,self.text_name_id).send_keys(name)
    def enter_confirm_password(self,password_confirm):
        self.driver.find_element(By.ID,self.text_confirm_password_id).send_keys(password_confirm)






