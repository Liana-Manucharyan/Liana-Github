import logging
import datetime
import pytest
from Pages.welcome import WelcomePage
from Pages.registration import RegistrationPage
from Pages.login import LoginPage
from Pages.home import HomePage
from Test_data import my_data

@pytest.mark.parametrize("course_name", my_data.existing_course_name)
def test_search_valid_course_check_title(driver, course_name):

    t_start = datetime.datetime.now()
    logging.info(f"Program has started at: {t_start}")

    welcome_obj = WelcomePage(driver)
    data = welcome_obj.parse_json_data("my_config.json")
    welcome_obj.navigate_to_url(data["url"])
    welcome_obj.go_to_login_page()
    
    register_obj = RegistrationPage(driver)
    login_obj = LoginPage(driver)

    if not data["login"]["email"] or not data["login"]["password"]:
        login_obj.go_to_register_page()
        register_obj.sign_up_to_app()
    else:
        login_obj.login_to_app(data["login"]["email"], data["login"]["password"])

    home_obj = HomePage(driver)
    home_obj.search_result(course_name) 
    result = home_obj.get_result_and_titles()
    home_obj.check_titles(result, course_name)

    t_end = datetime.datetime.now()
    logging.info(f"Program has ended at: {t_end}")
    logging.info(f"Program run duration is: {t_end - t_start}")
