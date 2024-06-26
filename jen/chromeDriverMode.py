from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def create_chrome_driver(headless=True, chrome_driver_path="C:\\webdrivers\\chromedriver.exe"): # chromedriver path is set here
    if headless:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
    else:
        if chrome_driver_path is None:
            raise ValueError("Chrome driver path is required for non-headless mode.")
        chrome_service = Service(chrome_driver_path)
        driver = webdriver.Chrome(service=chrome_service)
        driver.maximize_window()
    return driver