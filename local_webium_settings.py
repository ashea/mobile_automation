from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver import Firefox
from selenium.webdriver import Safari
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
import config


def update_chrome_options():
    new_option = ChromeOptions()
    new_option.add_argument('no-sandbox')
    wd = Chrome(options=new_option)
    return wd


if config.browser == 'Chrome':
    driver_class = update_chrome_options
elif config.browser == 'Safari':
    driver_class = Safari
elif config.browser == 'Firefox':
    driver_class = Firefox
else:
    raise WebDriverException("No browser specified")
implicit_timeout = 5
wait_timeout = 50

default_search_type = By.XPATH
