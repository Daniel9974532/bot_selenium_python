from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time


options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\chromedriver_win32\chromedriver.exe'

driver = webdriver.Chrome()

driver.get('https://www.leagueoflegends.com/es-mx/')
time.sleep(20)