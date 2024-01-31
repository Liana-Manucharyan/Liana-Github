from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging, os

class Helper:

    def __init__(self, browser):
        self.browser = browser

    def navigate_to_url(self, url):
        try:
            self.browser.get(url)
            self.browser.set_page_load_timeout(60)
            logging.info(f"Navigated to URL: '{url}'.")
        except Exception as e:
            logging.error(f"Exception in 'navigate_to_url': {e}")
            self.make_screenshot("go_to_page_screen.png")
    
    def find_and_send_keys(self, loc, inp_txt):
        try:
            elem = self.browser.find_element(*loc)
            elem.send_keys(inp_txt)
            logging.info(f"'{inp_txt}' text is entered in the search-box.")
        except Exception as e:
            logging.error(f"Exception in 'find_and_send_keys': {e}")
            self.make_screenshot("send_keys_screen.png")

    def find_and_click(self, loc, sec=150):
        try:
            elem = self.move_to_element(loc)
            WebDriverWait(self.browser, sec).until(EC.element_to_be_clickable(loc))
            elem.click()
        except Exception as e:
            logging.error(f"Exception in 'find_and_click': {e}")
            self.make_screenshot("find_and_click_screen.png")
    
    def move_to_element(self, loc):
        try:
            elem = self.browser.find_element(*loc)
            self.browser.execute_script("arguments[0].scrollIntoView();", elem) 
            return elem
        except Exception as e:
            logging.error(f"Exception in 'move_to_element': {e}")
            self.make_screenshot("move_to_elem_screen.png")

    def find_elems_dom(self, loc, sec=50):
        try:
            return WebDriverWait(self.browser, sec).until(EC.presence_of_all_elements_located(loc))
        except Exception as e:
            logging.error(f"Exception in 'find_elems_dom': {e}")
            self.make_screenshot("elem_in_dom_screen.png")
        
    def make_screenshot(self, file_name):
        self.browser.save_screenshot(os.path.join(os.path.dirname(__file__), file_name))
