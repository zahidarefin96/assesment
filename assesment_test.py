import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

# init driver
driver = webdriver.Chrome(
    executable_path="C:\\Users\\zahid\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)

# URL
driver.get("https://www.demoblaze.com/")

# creating sign-up
driver.find_element(By.XPATH, "//a[@id='signin2']").click()

driver.find_element(By.XPATH, "//input[@id='sign-username']").send_keys("sample_user123@gmail.com")

driver.find_element(By.XPATH, "//input[@id='sign-password']").send_keys("sampleuser123")

driver.find_element(By.XPATH, "//button[contains(text(),'Sign up')]").click()

driver.refresh()

# log-in and password
driver.find_element(By.XPATH, "//a[@id='login2']").click()

driver.find_element(By.XPATH, "//input[@id='loginusername']").send_keys("sample_user123@gmail.com")

driver.find_element(By.XPATH, " //input[@id='loginpassword']").send_keys("sampleuser123")

driver.find_element(By.XPATH, "//button[contains(text(),'Log in')]").click()

# Adding 2 items in the shopping cart
time.sleep(1)

driver.find_element(By.LINK_TEXT, "Samsung galaxy s7").click()

driver.find_element(By.XPATH, "//a[contains(text(),'Add to cart')]").click()

driver.refresh()

driver.find_element(By.XPATH, "//a[@id='nava']").click()

driver.find_element(By.LINK_TEXT, "Nokia lumia 1520").click()

driver.find_element(By.XPATH, "//a[contains(text(),'Add to cart')]").click()

driver.refresh()

driver.find_element(By.XPATH, "//a[contains(text(),'Cart')]").click()

driver.find_element(By.XPATH, "//button[contains(text(),'Place Order')]").click()

driver.find_element(By.XPATH, "//input[@id='name']").send_keys("sampleuser")

driver.find_element(By.XPATH, "//input[@id='country']").send_keys("samplecountry")

# click cancel
driver.back()

# click log-out
driver.find_element(By.XPATH, "//a[@id='logout2']").click()

# log-in and password again
driver.find_element(By.XPATH, "//a[@id='login2']").click()

driver.find_element(By.XPATH, "//input[@id='loginusername']").send_keys("sample_user@gmail.com")

driver.find_element(By.XPATH, " //input[@id='loginpassword']").send_keys("sampleuser123")

driver.find_element(By.XPATH, "//button[contains(text(),'Log in')]").click()

time.sleep(1)

driver.find_element(By.XPATH, "//a[@id='cartur']").click()

driver.find_element(By.XPATH, "//a[contains(text(),'Delete')]").click()

driver.quit()
