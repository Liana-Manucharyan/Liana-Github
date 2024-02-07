# Test Automation Framework for UltimateQA Course Search
This framework is designed for automated testing of the UltimateQA course search functionality.

## Main Test Scenario

1. Open a web browser and navigate to page: "https://courses.ultimateqa.com/collections"
2. If not registered, register to the application. If already registered, log in.
3. Search for existing course names, such as "Selenium" and "NodeJS".
4. Verify that the titles of the found courses contain the searched data.
5. Search for a non-existing course, such as "123".
6. Verify that the "No results were found" message is visible.

## Features
- Page Object Model (POM) pattern for better maintenance and readability.
- Two test cases implemented using PyTest:
  1. Search for an existing course and verify titles.
  2. Search for a non-existing course and verify error message.
- Exception handling and logging for better debugging.
- Allure reporting for detailed test reports.

## Project Structure
- `tests/`: Contains test cases.
- `pages/`: Contains page objects and locators.
- `helpers/`: Contains utility functions.
- `test_data/`: Contains test data files.
- `conftest/`: Contains fixtures and configuration files.
- `my_config.json`: Contains configuration data for the project.
- `allure_report_screen.png`: Screenshot of the Allure report.
- `requirements.txt`: Contains project dependencies.
- `README.md`: Detailed description of the project.

## Test cases:
### Helpers
general_functions.py        - navigate_to_url(url): Navigate to the specified URL.
                            - find_elems_in_dom(loc, sec=100): Find all elements located by the given locator in the DOM.
                            - find_elem_in_dom(loc, sec=100): Find an element located by the given locator in the DOM.
                            - find_and_send_keys(loc, inp_txt, sec=100): Find an input field, send input text, and log the action.
                            - scroll_and_click(loc, sec=100): Scroll to and click on an element.
                            - find_and_click(loc, sec=100): Find and click on an element.
                            - find_elem_in_ui(loc, sec=100): Find a visible element in the UI.
                            - get_elements(loc, sec=100): Find all elements located by the given locator.
                            - make_screenshot(file_name): Take a screenshot of the current window.
                            - parse_json_data(file_name): Parse JSON data from a file.
                            - write_json_data(file_name, data): Write JSON data to a file.

### Pages
home.py                     - get_search_result(course_names): Enter course names into the search box and submit.
                            - check_page_items(): Check if search results are found. Return the list of page items or "No results" message.
                            - add_items_to_list(page_items): Convert page items into a list of text.
                            - check_titles(search_text, item_text_list): Check if search text is found in all item texts.
                            - check_pages_and_get_titles(): Check each page for search results, scroll to the next page if available,   and gather all titles. Return a list of all titles.

login.py                    - go_to_register_page(): Navigate to the registration page by clicking the "Sign-up" link.
                            - login_to_app(email, password): Log in to the application using the provided email and password.

registration.py             - sign_up_to_app(): Register using predefined data and update login credentials. Logs the outcome.
                            - add_login_data_to_file(email, password): Update login data in the configuration file. Logs any errors.

welcome.py                  - go_to_login_page(): Navigate to the login page by clicking the "Login" link. Logs the action.

### Test_data
my_data.py                  - The stored data includes registration credentials and course search text

### Tests
test_existing_course_title_search.py    - The test case involves searching for valid course names and checking their titles.
test_non-existing_course_search.py      - The test case involves searching for a course with an invalid name and verifying that
                                        the "No results were found" message is displayed.

conftest.py                  - This code defines a pytest fixture named driver to create a Firefox WebDriver instance. It 
                            also sets up logging to save logs in 'my_log.log' with a specific format.


my_config.json               - The provided JSON configuration contains a URL for the website, along with login credentials which
                             are initially empty.
               
allure_report_screen.png     - Screenshot of the Allure report.

requirements.txt             - Contains project dependencies.
