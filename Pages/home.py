import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Helpers.general_functions import Helper
import time


class HomePage(Helper):

    search_box = (By.XPATH, "//input[@type='search']")
    no_search_result = (By.XPATH, "//p[contains(@class, 'no-results')]")
    search_result_list = (By.XPATH, "//li[@class='products__list-item']//div[@class='card__body']/h3")
    next_page = (By.XPATH, "//a[@aria-label='Next page']")

    has_next_page = True

    def search_result(self, course_names):
        try:
            search_field = self.find_and_send_keys(self.search_box, course_names)
            search_field.send_keys(Keys.ENTER)
            time.sleep(10)
        except Exception as e:
            logging.error(f"Error in 'search_and_check_result': {e}")       

    def get_result_and_titles(self):
        item_text_list = []
        while True:
            self.move_to_element(self.search_result_list)
            page_items = self.find_elems_in_dom(self.search_result_list)
            if page_items:
                for item in page_items:
                    item_text_list.append(item.text)
            else:
                no_result = self.find_elem_in_dom(self.no_search_result)
                return no_result.text.strip()            
            next_button = self.find_and_click(self.next_page)
            if not next_button:
                break  
        return item_text_list

    def check_titles(self, items_list, course_name):
        try:
            if items_list:
                for item in items_list:
                    if course_name in item:
                        logging.info(f"Course '{course_name}' found in item: {item}")
                    else:
                        logging.info(f"Course '{course_name}' not found in item: {item}.")
                        break
            else:
                logging.info("No items to check.")
        except Exception as e:
            logging.error(f"Error while checking titles: {e}")
