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

    def get_search_result(self, course_names):
        search_field = self.find_and_send_keys(self.search_box, course_names)
        search_field.send_keys(Keys.ENTER)
        time.sleep(20)

    def check_page_items(self):
        page_items = self.find_elems_in_dom(self.search_result_list)
        if page_items:
            logging.info("Search results are found.")
            return page_items
        else:
            no_result = self.find_elem_in_dom(self.no_search_result)
            return no_result.text.strip()    
    
    def add_items_to_list(self, page_items):
        return [item.text for item in page_items]

    def check_titles(self, search_text, item_text_list):
        try:
            if all(search_text.lower() in item.lower() for item in item_text_list):
                logging.info(f"Course '{search_text}' found in all items.")
            else:
                logging.info(f"Course '{search_text}' not found in all items.")
        except Exception as e:
            logging.error(f"Error in 'check_titles': {e}")

    def check_pages_and_get_titles(self):
        all_titles_set = set()
        page_items = self.check_page_items()
        if page_items:
            all_titles_set.update(self.add_items_to_list(page_items))
            while len(self.get_elements(self.next_page)) > 0:
                self.scroll_and_click(self.next_page)
                logging.info("'Next page' button is clicked.")
                page_items = self.check_page_items()
                if page_items:
                    new_titles = set(self.add_items_to_list(page_items))  
                    all_titles_set.update(new_titles)  
            all_titles = list(all_titles_set)  
            titles_list = "\n".join(all_titles)
            logging.info(f"List of all titles: '{titles_list}'")
            return all_titles
