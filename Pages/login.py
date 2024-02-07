import logging
from selenium.webdriver.common.by import By
from Helpers.general_functions import Helper


class LoginPage(Helper):
    
    lnk_new_account = (By.XPATH, "//a[contains(@href, 'sign_up')]")
    inp_email = (By.ID, "user[email]")
    inp_password = (By.ID, "user[password]")
    btn_sign_in = (By. XPATH, "//button[@type='submit']")

    def go_to_register_page(self):
        try:
            self.find_and_click(self.lnk_new_account)
            logging.info("'Sign-up' page is opened.")
        except Exception as e:
            logging.error(f"Error in 'go_to_register_page': {e}")
            self.save_screenshot("go_to_register_pag_screen.png")   

    def login_to_app(self, email, password):
        try:
            self.find_and_send_keys(self.inp_email, email)
            self.find_and_send_keys(self.inp_password, password)
            self.find_and_click(self.btn_sign_in) 
            logging.info("Logged in successfully!!!") 
        except Exception as e:
            logging.error(f"Error in 'login_to_app': {e}") 
            self.save_screenshot("login_to_app_screen.png")        
            