from selenium import webdriver
import pytest
import logging


@pytest.fixture()
def driver():
    try:
        driver = webdriver.Firefox()
        logging.info(f"'{driver.name.capitalize()}' browser is opened.")
        driver.maximize_window()
        yield driver
        driver.quit()
        logging.info(f"'{driver.name.capitalize()}' browser is closed.")
    except Exception as e:
        logging.error(f"Error: {e}")


def pytest_configure():
    logging.basicConfig(filename= "my_log.log",
                        level=logging.INFO,
                        format='%(asctime)s %(levelname)s - %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S'
                        )
    