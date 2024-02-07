import logging
import datetime
from Pages.welcome import WelcomePage
from Pages.registration import RegistrationPage
from Pages.login import LoginPage
from Pages.home import HomePage
from Test_data import my_data


def test_search_with_invalid_course_name(driver):
    
    t_start = datetime.datetime.now()
    logging.info(f"Program has started at: {t_start}")

    welcome_obj = WelcomePage(driver)
    data = welcome_obj.parse_json_data("my_config.json")
    welcome_obj.navigate_to_url(data["url"])
    welcome_obj.go_to_login_page()
    
    register_obj = RegistrationPage(driver)
    login_obj = LoginPage(driver)

    if data["login"]["email"] == "" and data["login"]["password"] == "":
        login_obj.go_to_register_page()
        register_obj.sign_up_to_app()
    else:
        login_obj.login_to_app(data["login"]["email"], data["login"]["password"])

    home_obj = HomePage(driver)
    home_obj.get_search_result(my_data.no_existing_course_name)
    search_result = home_obj.check_page_items()
    assert search_result == "No results were found"
    logging.info(f"No courses found with '{my_data.no_existing_course_name}' key.")

    t_end = datetime.datetime.now()
    logging.info(f"Program has ended at: {t_end}")
    logging.info(f"Program run duration is: {t_end - t_start}")
