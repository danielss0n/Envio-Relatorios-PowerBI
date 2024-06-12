import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import win32com.client as win32
import time

DRIVER_PATH = "chromedriver.exe"

service = webdriver.ChromeService(executable_path=DRIVER_PATH)
options = webdriver.ChromeOptions()
options.add_argument(f"user-data-dir=C:/Users/{os.getenv('USERNAME')}/AppData/Local/Google/Chrome/User Data")
driver = webdriver.Chrome(service=service, options=options)

def save_print(folder, file_name): 
    print = driver.get_screenshot_as_png()
    with open(f'prints/{folder}/{file_name}.png', 'wb') as file:
        file.write(print)

def wait_to_click(xpath):
    WebDriverWait(driver, 999).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()