from selenium.webdriver.common.by import By
from helpers import Helper
import logging, datetime

def test_auto_web_search(driver):

    t_start = datetime.datetime.now()
    logging.info(f"Program has started at: {t_start}")

    url = "https://auto.am/"
    search_text = "Infiniti"
    inp_text_loc = (By.ID, "searchInp")
    btn_submit_loc = (By.XPATH, "//i[@id='submit_search']")
    lst_result_loc = (By.XPATH, "//div[@id='search-result']//div[contains(@class, 'card ')]")

    helper_obj = Helper(driver)
    helper_obj.navigate_to_url(url)  
    helper_obj.find_and_send_keys(inp_text_loc, search_text)
    helper_obj.find_and_click(btn_submit_loc)
    search_result = helper_obj.find_elems_dom(lst_result_loc)
    assert len(search_result) > 0
    logging.info(f"'{len(search_result)}' results found for search '{search_text}' text.")

    t_end = datetime.datetime.now()
    logging.info(f"Program has ended at: {t_end}")
    logging.info(f"Program run duration is: {t_end - t_start}")
