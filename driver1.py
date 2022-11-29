from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time

#from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

#driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url = "google.com"

driver.get('google.com');
time.sleep(10);
time.sleep(5);
driver.close();

#driver.close()
#driver.quit()
#driver.dispose()

