import configparser

config=configparser.RawConfigParser()
config.read("./Configurations/config.ini")

class ReadConfigClass:
    @staticmethod
    def get_data_for_email():
        email=config.get('login_data','email')
        return email

    @staticmethod
    def get_data_for_password():
        password=config.get('login_data','password')
        return password
    @staticmethod
    def get_homepage_url():
        home_page_url=config.get('app_urls','home_page_url')
        return home_page_url
    @staticmethod
    def get_login_url():
        login_url=config.get('app_urls','login_url')
        return login_url
    @staticmethod
    def get_registration_url():
        registration_url=config.get('app_urls','registration_url')
        return registration_url





