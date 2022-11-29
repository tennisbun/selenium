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

driver.get("http://localhost:5173")

#emailInput2 = driver.find_element(By.ID, "emailInput")
emailInput = driver.find_element(By.CLASS_NAME, "emailInput")
fnInput = driver.find_element(By.CLASS_NAME, "fnInput") 
pwdInput = driver.find_element(By.CLASS_NAME, "pwdInput")
pwdcfInput = driver.find_element(By.CLASS_NAME, "pwdcfInput")
submitButton = driver.find_element(By.CLASS_NAME, "submitButton")

emailInput.send_keys("test@gmail.com")
fnInput.send_keys("Mike Wazowski")
pwdInput.send_keys("f4z3r77");
pwdcfInput.send_keys("f4z3r77");
print(emailInput);
time.sleep(5);
submitButton.click();
time.sleep(20);
driver.close();

#driver.close()
#driver.quit()
#driver.dispose()

