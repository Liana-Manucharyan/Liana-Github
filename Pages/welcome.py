import logging
from selenium.webdriver.common.by import By
from Helpers.general_functions import Helper


class WelcomePage(Helper):
    
    lnk_login_loc = (By.XPATH, "//a[contains(@href, 'sign_in')]")
    
    def go_to_login_page(self):
        try:
            self.find_and_click(self.lnk_login_loc)
            logging.info("'Login' page is opened.")
        except Exception as e:
            logging.error(f"Error in 'go_to_login_page': {e}")
            self.save_screenshot("go_to_login_page_screen.png") 
