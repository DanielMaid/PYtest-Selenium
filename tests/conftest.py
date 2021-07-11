import pytest
from selenium import webdriver

from config.config import Config


@pytest.fixture(scope='class')
def init_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    driver = webdriver.Chrome(options=options, executable_path=Config.CHROME_PATH)
    driver.maximize_window()
    driver.get(Config.BASE_URL)
    yield driver
    driver.quit()
