import logging
import os
import json
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class Helper:

    def __init__(self, browser):
        self.browser = browser

    def navigate_to_url(self, url):
        try:
            self.browser.get(url)
            self.browser.set_page_load_timeout(100)
            logging.info(f"Navigated to URL: '{url}'")
        except Exception as e:
            logging.error(f"Error in 'navigate_to_url': {e}")

    def move_to_element(self, loc):
        try:
            elem = self.browser.find_element(*loc)
            self.browser.execute_script("arguments[0].scrollIntoView();", elem)
            return elem
        except Exception as e:
            logging.error(f"Error in 'move_to_element': {e}")
            self.make_screenshot("move_to_elem_screen.png")

    def mouse_hover(self, loc):
        try:
            elem = self.browser.find_element(*loc)
            actions = ActionChains(self.browser)
            actions.move_to_element(elem).perform()
        except Exception as e:
            logging.error(f"Error in 'mouse_hover': {e}")
            self.make_screenshot("mouse_hover_screen.png")

    def find_elems_in_dom(self, loc, sec=100):
        try:
            return WebDriverWait(self.browser, sec).until(EC.presence_of_all_elements_located(loc))
        except Exception as e:
            logging.error(f"Error in 'find_elems_in_dom': {e}")

    def find_elem_in_dom(self, loc, sec=100):
        try:
            return WebDriverWait(self.browser, sec).until(EC.presence_of_element_located(loc))
        except Exception as e:
            logging.error(f"Error in 'find_elem_in_dom': {e}")

    def find_and_send_keys(self, loc, inp_txt, sec=100):
        try:
            elem = WebDriverWait(self.browser, sec).until(EC.visibility_of_element_located(loc))
            elem.send_keys(inp_txt)
            name_attribute_value = elem.get_attribute("name")
            logging.info(f"'{inp_txt}' text is entered in name: '{name_attribute_value}' input field.")
            return elem
        except Exception as e:
            logging.error(f"Error in 'find_and_send_keys': {e}")

    def scroll_and_click(self, loc, sec=100):
        try:         
            elem = WebDriverWait(self.browser, sec).until(EC.element_to_be_clickable(loc))
            self.browser.execute_script("arguments[0].click();", elem)
            logging.info(f"'{elem.text}' button is scrolled to.")
            logging.info(f"'{elem.text}' button is clicked.")
            elem.click()
        except Exception as e:
            logging.error(f"Error in 'find_and_click': {e}")

    def find_and_click(self, loc, sec=100):
        try: 
            self.find_elem_in_ui(loc)    
            elem = WebDriverWait(self.browser, sec).until(EC.element_to_be_clickable(loc))
            logging.info(f"'{elem.text}' button is clicked.")
            elem.click()
        except Exception as e:
            logging.error(f"Error in 'find_and_click': {e}")        

    def find_elem_in_ui(self, loc, sec=100):
        try:
            return WebDriverWait(self.browser, sec).until(EC.visibility_of_element_located(loc))
        except Exception as e:
            logging.error(f"Error in 'find_elem_in_ui': {e}")

    def get_elements(self, loc, sec=100):
            elem = self.browser.find_elements(*loc)
            return elem

    def find_elems_in_ui(self, loc, sec=100):
        try:
            return WebDriverWait(self.browser, sec).until(EC.visibility_of_all_elements_located(loc))
        except Exception as e:
            logging.error(f"Error in 'find_elems_in_ui': {e}")

    def make_screenshot(self, file_name):
        self.browser.save_screenshot(os.path.join(os.path.dirname(__file__), file_name))    

    def parse_json_data(self, file_name):
        try:
            config_path = os.path.join(os.path.dirname(__file__), '..', file_name)
            with open(config_path, 'r') as file:
                json_data = json.load(file)
                logging.info(f"Loaded JSON data: {json_data}.")
                return json_data
        except Exception as e:
            logging.error(f"Error in 'parse_json_data': {e}")   

    def wait_for_search_results(self, *elems):
        try:
            WebDriverWait(self.browser, 100).until(
                EC.presence_of_element_located(elems[0]) or 
                EC.presence_of_element_located(elems[1])
            )
        except Exception as e:
            logging.error(f"Error in 'wait_for_search_results': {e}")     
            
    def write_json_data(self, file_name, data):
        try:
            config_path = os.path.join(os.path.dirname(__file__), '..', file_name)
            with open(config_path, 'w') as file:
                json.dump(data, file, indent=4)
                logging.info(f"JSON data written to file '{file_name}'")
        except Exception as e:
            logging.error(f"Error in 'write_json_data': {e}")      
