import allure
import pytest
from faker import Faker
from utilities.Logger import LogGeneratorClass
from utilities.Read_config import ReadConfigClass
from pageObjects.Login_page import LoginPage
from pageObjects.Registration_page import RegistrationPage


@pytest.mark.usefixtures("browser_setup") # new
class TestUserLogin001:
    driver=None
    email=ReadConfigClass.get_data_for_email()
    password=ReadConfigClass.get_data_for_password()
    homepage_url=ReadConfigClass.get_homepage_url()
    login_url=ReadConfigClass.get_login_url()
    registration_url=ReadConfigClass.get_registration_url()
    log=LogGeneratorClass.log_generator()


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Verify the Application url title")
    @allure.description("This testcase is to validate credkart title functionality")
    @allure.link(homepage_url)
    @allure.story("Story1")
    @allure.epic("Epic1")
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.sanity

    def test_credkart_url_001(self):

        self.log.info("Test credkart 001 is started")
        self.driver.get(self.homepage_url)
        self.log.info(f"Opening browser and landing on {self.homepage_url}")
        self.log.info("Checking url title")
        if self.driver.title=="CredKart":
            self.log.info(f"Page title is correct and landed on url {self.driver.title}")
            self.log.info("Taking Screenshot")
            self.driver.save_screenshot(".\\Screenshots\\Cred_kart_home_Page_PAss.png")
            allure.attach.file(
                ".\\Screenshots\\Cred_kart_home_Page_PAss.png",name="Credkart_Home_page_Pass",
                attachment_type=allure.attachment_type.PNG
            )
            self.log.info("Test case 'test_credkart_url_001' is Pass")
        else:
            self.log.info(f"Page title is correct and landed on url --> {self.driver.title}")
            self.log.info("Taking Screenshot")
            self.driver.save_screenshot(".\\Screenshots\\Cred_kart_Home_Page.png")
            self.log.info("Test case 'test_credkart_url_001' is Fail")
            assert False
        self.log.info("Test case 'test_credkart_url_001' is completed")

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Verify the login")
    @allure.description("This testcase is to validate credkart login functionality")
    @allure.link(login_url)

    def test_credkart_login_002(self):
        self.log.info("Test case 'test_credkart_login_002' is started")
        self.driver.get(self.login_url)
        self.log.info(f"Launching browser and landing on {self.login_url}")
        self.lp=LoginPage(self.driver)
        # Enter email
        self.log.info(f"Entering email {self.email}")
        self.lp.enter_email(self.email)
        #  Enter Password
        self.log.info(f"Entering password ********")
        self.lp.enter_password(self.password)
        self.lp.click_submit()
        self.log.info("Checking login status")
        if self.lp.verify_menu()=="Pass":
            self.log.info("Login Pass")
            self.lp.click_menu()
            self.lp.click_logout()
            self.log.info(f"Testcase 'test_credkart_login_002' Pass")
        else:
            self.log.info("Login Fail")
            self.log.info("Taking Screenshot for fail testcase")
            self.driver.save_screenshot(".\\Screenshots\\Cred_kart_Home_Page.png")
            allure.attach.file(".\\Screenshots\\Cred_kart_Home_Page.png.png",name="Credkart_login_fail",
                attachment_type=allure.attachment_type.PNG)
            assert False
        self.log.info(f"Testcase 'test_credkart_login_002' completed")

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Verify the registration")
    @allure.description("This testcase is to validate credkart user registration functionality")
    @allure.link(registration_url)
    def test_credkart_registration_003(self):
        self.log.info("Test case 'test_credkart_registration_003' is started")
        self.driver.get(self.registration_url)
        self.log.info(f"Launching browser and landing on {self.registration_url}")

        self.driver.maximize_window()

        name_data =Faker().name()
        print(f"name_data-->{name_data}")

        email_data = Faker().email()
        print(f"email_data-->{email_data}")

        self.rp=RegistrationPage(self.driver)
        self.lp = LoginPage(self.driver)
        self.rp.enter_name(name_data)


        # Enter Email
        self.log.info(f"Entering email {self.email}")
        self.lp.enter_email(email_data)

        # Enter Password
        self.log.info(f"Entering password ********")
        self.lp.enter_password(self.password)

        # Enter Confirm Password
        self.log.info(f"Entering confirm-password ********")
        self.rp.enter_confirm_password(self.password)

        # Click Register Button
        self.lp.click_submit()
        # Verify Registration
        self.log.info("checking registration status")
        if self.lp.verify_menu() == "Pass":
            self.log.info("Registration Pass")
            self.lp.click_menu()
            self.lp.click_logout()
            self.log.info("Taking Screenshot for pass testcase")
            self.driver.save_screenshot(".\\Screenshots\\User_registration_pass.png")
        else:
            self.log.info("Registration Fail")
            self.log.info("Taking Screenshot for fail testcase")
            self.driver.save_screenshot(".\\Screenshots\\User_registration_fail.png")
            assert False
        self.log.info(f"Testcase 'test_credkart_registration_003' completed")



        self.driver.quit()


#  pytest -v -s --alluredir="AllureReports"
# allure serve "AllureReports"