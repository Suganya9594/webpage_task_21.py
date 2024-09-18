from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# open the Chrome driver
driver = webdriver.Chrome()

# Open the SauceDemo website
driver.get("https://www.saucedemo.com/")

# Display cookies before login
print("Cookies before login:")
print(driver.get_cookies())
time.sleep(5)

# entering the username 
driver.find_element(By.ID, "user-name").send_keys("standard_user")
time.sleep(3)
           
# entering the password           )
driver.find_element(By.ID, "password").send_keys("secret_sauce")
time.sleep(3)

# Clicking the login button
driver.find_element(By.ID, "login-button").click()
time.sleep(3)

# Wait for the dashboard to load
time.sleep(3)

# Display cookies after login
print("Cookies after login:")
print(driver.get_cookies())
time.sleep(5)

# Perform logout
driver.find_element(By.ID, "react-burger-menu-btn").click()
time.sleep(5)
driver.find_element(By.ID, "logout_sidebar_link").click()

# Wait for the logout to complete
time.sleep(3)

# Display cookies after logout
print("Cookies after logout:")
print(driver.get_cookies())
time.sleep(3)

# Close the browser
driver.quit()
