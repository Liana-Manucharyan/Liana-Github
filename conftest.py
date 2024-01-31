from selenium import webdriver
import pytest
import logging, os

@pytest.fixture()
def driver():
    try:
        driver = webdriver.Chrome()
        logging.info(f"'{driver.name.capitalize()}' browser is opened.")
        driver.maximize_window()
        yield driver
        driver.quit()
        logging.info(f"'{driver.name.capitalize()}' browser is closed.")
    except Exception as e:
        logging.error(f"Error: {e}")


def pytest_configure():
  
    logging.basicConfig(level=logging.INFO,  
                        format='%(asctime)s - %(levelname)s - %(message)s',  
                        datefmt='%Y-%m-%d %H:%M:%S',
                        filename=os.path.join(os.path.dirname(__file__), "logs.log"),
                        filemode = "a",
                        encoding='utf-8'
                        )
    