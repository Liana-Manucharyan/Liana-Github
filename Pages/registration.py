import logging
from selenium.webdriver.common.by import By
from Helpers.general_functions import Helper
from Test_data import my_data


class RegistrationPage(Helper):
    
    inp_f_name = (By.ID, "user[first_name]")
    inp_l_name = (By.ID, "user[last_name]")
    inp_email = (By.ID, "user[email]")
    inp_password = (By.ID, "user[password]")
    checkbox_terms = (By.ID, "user[terms]")
    btn_register = (By.XPATH, "//button[contains(text(),'Sign up')]")
    
    def sign_up_to_app(self):
        try:
            self.find_and_send_keys(self.inp_f_name, my_data.first_name)
            self.find_and_send_keys(self.inp_l_name, my_data.last_name)
            self.find_and_send_keys(self.inp_email, my_data.email)
            self.find_and_send_keys(self.inp_password, my_data.password)
            self.find_and_click(self.checkbox_terms)
            self.scroll_and_click(self.btn_register)
            self.add_login_data_to_file(my_data.email, my_data.password)
            logging.info("Registered successfully!!!")
            logging.info("Home page is opened.")
        except Exception as e:
            logging.error(f"Error in 'sign_up_to_app': {e}")
            self.save_screenshot("sign_up_to_app_screen.png")  
    
    def add_login_data_to_file(self, email, password):
        try:
            data = self.parse_json_data("my_config.json")
            data["login"]['email'] = email
            data["login"]['password'] = password
            logging.info(f"Login data: Email: '{email}', Password: '{password}'.")
            self.write_json_data("my_config.json", data)
        except Exception as e:
            logging.error(f"Error in 'add_login_data_to_file': {e}")
            self.save_screenshot("add_login_data_to_file_screen.png") 
